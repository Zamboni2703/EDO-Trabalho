#!/usr/bin/env python3
"""
Gera cada equação dos slides como PNG transparente (KaTeX + Chrome headless).
Equações extraídas automaticamente do slides.html. Para ser rápido, renderiza
TODAS numa única página (uma por linha), tira um screenshot de página inteira e
recorta cada equação pela sua faixa vertical. Uma única chamada ao Chrome.

Saída: eq_img/eq_<hash>.png (transparente, recortado) + eq_map.json
"""
import os, re, json, subprocess, hashlib, html as H
os.environ.setdefault("MPLCONFIGDIR", "/tmp/mplconfig")
import numpy as np
import pymupdf

BASE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(BASE, "eq_img")
os.makedirs(OUT, exist_ok=True)
CHROME, SCALE, COLOR = "chrome", 3, "#2b2b2b"

def extract_eqs():
    src = open(os.path.join(BASE,"slides.html"), encoding="utf-8").read()
    eqs = {}
    for m in re.finditer(r'data-eq="((?:[^"\\]|\\.)*)"', src):
        eqs.setdefault(H.unescape(m.group(1)), False)
    for m in re.finditer(r'data-eq-display="((?:[^"\\]|\\.)*)"', src):
        eqs[H.unescape(m.group(1))] = True
    return eqs

def key(tex):
    return "eq_" + hashlib.md5(tex.encode()).hexdigest()[:12]

PAGE = """<!DOCTYPE html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="katex/katex.min.css">
<style>
 html,body{margin:0;padding:0;background:transparent;}
 .row{display:block;height:180px;line-height:180px;white-space:nowrap;padding-left:20px;color:__COLOR__;}
 .row .katex{font-size:40px;line-height:normal;}
 .row.d .katex{font-size:44px;}
</style></head><body>
<div id="host">__ROWS__</div>
<script src="katex/katex.min.js"></script>
<script>
 document.querySelectorAll('.row').forEach(function(el){
   katex.render(el.getAttribute('data-tex'), el,
     {throwOnError:false, displayMode: el.classList.contains('d')});
 });
 window.__done=true;
</script></body></html>"""

def build_page(items):
    rows=[]
    for tex,disp in items:
        cls = "row d" if disp else "row"
        rows.append(f'<div class="{cls}" data-tex="{H.escape(tex)}"></div>')
    return PAGE.replace("__COLOR__", COLOR).replace("__ROWS__", "\n".join(rows))

ONE = """<!DOCTYPE html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="katex/katex.min.css">
<style>
 html,body{margin:0;padding:0;background:transparent;}
 #eq{display:inline-block;padding:6px 10px;color:__COLOR__;}
 .katex{font-size:__FS__px;}
</style></head><body><span id="eq"></span>
<script src="katex/katex.min.js"></script>
<script>
 katex.render(__TEX__, document.getElementById("eq"),
   {throwOnError:false, displayMode:__DISP__});
 window.__done=true;
</script></body></html>"""

def one_page(tex, disp, fs):
    return (ONE.replace("__COLOR__",COLOR).replace("__FS__",str(fs))
               .replace("__TEX__", json.dumps(tex))
               .replace("__DISP__","true" if disp else "false"))

def crop_one(path, pad=10):
    p = pymupdf.Pixmap(path)
    arr = np.frombuffer(p.samples, dtype=np.uint8).reshape(p.height,p.width,p.n)
    ys,xs = np.where(arr[:,:,-1] > 8)
    if len(xs)==0: return None
    x0,x1 = max(0,xs.min()-pad), min(p.width, xs.max()+pad+1)
    y0,y1 = max(0,ys.min()-pad), min(p.height, ys.max()+pad+1)
    sub = np.ascontiguousarray(arr[y0:y1, x0:x1, :])
    h,w = sub.shape[:2]
    out = pymupdf.Pixmap(pymupdf.csRGB, pymupdf.IRect(0,0,w,h), True)
    out.samples_mv[:] = sub.tobytes()
    out.save(path)
    return w, h

def main():
    import sys
    env = dict(os.environ, HOME="/projects/sandbox")
    eqs = sorted(extract_eqs().items())
    mapfile = os.path.join(BASE,"eq_map.json")
    mp = json.load(open(mapfile)) if os.path.exists(mapfile) else {}
    # argumentos opcionais: start end  (para fatiar entre chamadas)
    start = int(sys.argv[1]) if len(sys.argv)>1 else 0
    end   = int(sys.argv[2]) if len(sys.argv)>2 else len(eqs)
    hp = os.path.join(BASE, "_eqtmp.html")
    for i in range(start, min(end,len(eqs))):
        tex,disp = eqs[i]
        fs = 44 if disp else 40
        open(hp,"w",encoding="utf-8").write(one_page(tex,disp,fs))
        k = key(tex); png = os.path.join(OUT, f"{k}.png")
        subprocess.run([CHROME,"--headless","--no-sandbox","--disable-gpu",
            "--default-background-color=00000000",
            f"--force-device-scale-factor={SCALE}",
            "--window-size=2400,520","--virtual-time-budget=3000",
            f"--screenshot={png}", f"file://{hp}"],
            env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        r = crop_one(png)
        if r:
            w,h = r
            mp[tex] = {"file": f"eq_img/{k}.png", "w": round(w/SCALE,1),
                       "h": round(h/SCALE,1), "display": disp}
    json.dump(mp, open(mapfile,"w"), indent=1, ensure_ascii=False)
    if os.path.exists(hp): os.remove(hp)
    print(f"faixa [{start}:{end}] feita. total no mapa: {len(mp)}/{len(eqs)}")

if __name__ == "__main__":
    main()
