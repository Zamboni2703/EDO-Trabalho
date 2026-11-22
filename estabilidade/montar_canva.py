#!/usr/bin/env python3
"""
Gera slides_canva.html: igual ao slides.html, mas cada equação vira um <img>
(PNG transparente da pasta eq_img). O texto continua texto editável. Imprime em
PDF depois. No Canva: texto = texto (você muda tamanho), equação = imagem que
não quebra e que você redimensiona (= mudar o tamanho da fonte da conta).
"""
import os, re, json, html as H

BASE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(BASE,"slides.html"), encoding="utf-8").read()
mp  = json.load(open(os.path.join(BASE,"eq_map.json"), encoding="utf-8"))

# altura-alvo de uma equação inline no corpo (px). Corpo do texto ~25px.
# Equações "baixas" (1 linha) ~ 30px; equações com fração (altas) um pouco maiores
# para não ficarem espremidas na linha.
INLINE_H      = 30     # altura de uma equação simples (1 linha)
INLINE_H_FRAC = 46     # altura para equações com fração/raiz (nativo alto)
FRAC_THRESH   = 60     # px nativos de altura acima do qual tratamos como "fração"
DISPLAY_SCALE = 0.46   # escala das equações em display (px nativos CSS do crop)

miss=[0]
def repl_inline(m):
    tex = H.unescape(m.group(1))
    info = mp.get(tex)
    if not info:
        miss[0]+=1; return m.group(0)
    # frações/raízes inline (altura nativa grande) ganham altura maior
    h = INLINE_H_FRAC if info["h"] > FRAC_THRESH else INLINE_H
    w = info["w"]*(h/info["h"])
    va = "-30%" if info["h"] > FRAC_THRESH else "-22%"
    return (f'<img class="eqi" src="{info["file"]}" '
            f'style="height:{h:.0f}px;width:{w:.0f}px;vertical-align:{va};" alt="eq">')

def repl_display(m):
    tex = H.unescape(m.group(1))
    info = mp.get(tex)
    if not info:
        miss[0]+=1; return m.group(0)
    w = info["w"]*DISPLAY_SCALE
    h = info["h"]*DISPLAY_SCALE
    return (f'<img class="eqd" src="{info["file"]}" '
            f'style="height:{h:.0f}px;width:{w:.0f}px;" alt="eq">')

out = re.sub(r'<span[^>]*\bdata-eq="((?:[^"\\]|\\.)*)"[^>]*>\s*</span>', repl_inline, src)
out = re.sub(r'<div[^>]*\bdata-eq-display="((?:[^"\\]|\\.)*)"[^>]*>\s*</div>', repl_display, out)

# remove scripts do KaTeX (não precisamos mais)
out = re.sub(r'<script src="katex/katex.min.js">\s*</script>', '', out)
out = re.sub(r'<script>\s*//[^\n]*\n(?:.*?\n)*?\s*window\.__katexDone = true;\s*</script>', '', out, flags=re.S)
# remove o link do katex.css (equações agora são imagens)
out = out.replace('<link rel="stylesheet" href="katex/katex.min.css">', '')

css_extra = """
<style>
 .eqd{display:block;margin:14px auto;}
 .eq-grande{line-height:0;}
 .eqi{display:inline-block;}
</style>"""
out = out.replace('</head>', css_extra + '\n</head>')

open(os.path.join(BASE,"slides_canva.html"),"w",encoding="utf-8").write(out)
rem = len(re.findall(r'data-eq(?:-display)?="', out))
print(f"slides_canva.html gerado. não convertidas: {miss[0]} | data-eq restantes: {rem}")
