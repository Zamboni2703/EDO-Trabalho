#!/usr/bin/env python3
"""
Converte roteiro_fala.md -> roteiro_fala.docx, preservando:
 títulos (#, ##, ###), listas (- e aninhadas), negrito **..**, código `..`,
 citações (>) e separadores (---). Formatação limpa, pronta para o Word.
"""
import os, re
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

BASE = os.path.dirname(os.path.abspath(__file__))
MD   = os.path.join(BASE, "roteiro_fala.md")
OUT  = os.path.join(BASE, "roteiro_fala.docx")

SLATE = RGBColor(0x5b, 0x69, 0x75)
GREY  = RGBColor(0x55, 0x55, 0x55)

doc = Document()
# fonte base
normal = doc.styles["Normal"]
normal.font.name = "Calibri"
normal.font.size = Pt(11)

def add_runs(paragraph, text):
    """Interpreta **negrito** e `código` dentro de uma linha."""
    # tokeniza mantendo delimitadores
    parts = re.split(r'(\*\*.+?\*\*|`[^`]+`)', text)
    for part in parts:
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            r = paragraph.add_run(part[2:-2]); r.bold = True
        elif part.startswith("`") and part.endswith("`"):
            r = paragraph.add_run(part[1:-1])
            r.font.name = "Consolas"; r.font.size = Pt(10.5)
            r.font.color.rgb = RGBColor(0x1a,0x4b,0x8c)
        else:
            paragraph.add_run(part)

lines = open(MD, encoding="utf-8").read().splitlines()
i = 0
# juntar linhas de parágrafo quebradas em várias linhas do md (wrap)
while i < len(lines):
    raw = lines[i]
    line = raw.rstrip()
    stripped = line.strip()

    if stripped == "":
        i += 1; continue

    # separador
    if re.fullmatch(r'-{3,}', stripped):
        p = doc.add_paragraph()
        p.paragraph_format.border_bottom = True  # fallback; adiciona linha fina
        pr = p.add_run("―" * 40); pr.font.color.rgb = GREY
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        i += 1; continue

    # títulos
    m = re.match(r'(#{1,6})\s+(.*)', stripped)
    if m:
        level = len(m.group(1)); txt = m.group(2)
        if level == 1:
            h = doc.add_heading(level=0)   # título
            r = h.add_run(txt); r.font.color.rgb = SLATE
        else:
            h = doc.add_heading(level=min(level-1, 4))
            for run in list(h.runs): run.text = ""
            add_runs(h, txt)
            for run in h.runs: run.font.color.rgb = SLATE
        i += 1; continue

    # citação (bloco >)
    if stripped.startswith(">"):
        buf = []
        while i < len(lines) and lines[i].strip().startswith(">"):
            buf.append(lines[i].strip().lstrip(">").strip())
            i += 1
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.3)
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(8)
        add_runs(p, " ".join(buf))
        for run in p.runs:
            run.italic = True; 
            if run.font.color.rgb is None: run.font.color.rgb = GREY
        continue

    # lista (- item), com possível continuação indentada
    m = re.match(r'(\s*)-\s+(.*)', raw)
    if m:
        indent = len(m.group(1))
        txt = m.group(2)
        # junta continuação (linhas seguintes indentadas que não são novo item/título)
        j = i + 1
        while j < len(lines):
            nxt = lines[j]
            if nxt.strip() == "" or re.match(r'\s*-\s+', nxt) or re.match(r'#{1,6}\s', nxt.strip()) or re.fullmatch(r'-{3,}', nxt.strip()):
                break
            txt += " " + nxt.strip()
            j += 1
        style = "List Bullet 2" if indent >= 2 else "List Bullet"
        try:
            p = doc.add_paragraph(style=style)
        except KeyError:
            p = doc.add_paragraph(style="List Bullet")
        add_runs(p, txt)
        i = j; continue

    # parágrafo normal (junta linhas até linha em branco/elemento)
    buf = [stripped]
    j = i + 1
    while j < len(lines):
        nxt = lines[j]
        if (nxt.strip() == "" or re.match(r'#{1,6}\s', nxt.strip())
                or re.match(r'\s*-\s+', nxt) or nxt.strip().startswith(">")
                or re.fullmatch(r'-{3,}', nxt.strip())):
            break
        buf.append(nxt.strip()); j += 1
    p = doc.add_paragraph()
    add_runs(p, " ".join(buf))
    i = j

doc.save(OUT)
print("gerado:", OUT)
