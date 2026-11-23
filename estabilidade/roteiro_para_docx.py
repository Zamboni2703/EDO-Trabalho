#!/usr/bin/env python3
"""
Converte roteiro_falado.md -> Roteiro_Estabilidade_JoaoGabriel.docx
no mesmo estilo dos roteiros de Otimização Inteira do João:
 - capa (primeiras linhas) centralizada
 - cabeçalhos "SLIDE N — ... (~tempo)" em negrito
 - linhas "Dica:" em itálico/cinza
 - separador de régua
 - seção "Possíveis perguntas" com perguntas em negrito e respostas (→) normais
"""
import os, re
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

BASE = os.path.dirname(os.path.abspath(__file__))
MD   = os.path.join(BASE, "roteiro_falado.md")
OUT  = os.path.join(BASE, "Roteiro_Estabilidade_JoaoGabriel.docx")

SLATE = RGBColor(0x5b, 0x69, 0x75)
GREY  = RGBColor(0x66, 0x66, 0x66)

doc = Document()
st = doc.styles["Normal"]
st.font.name = "Calibri"
st.font.size = Pt(11)
st.paragraph_format.space_after = Pt(8)
st.paragraph_format.line_spacing = 1.15

lines = open(MD, encoding="utf-8").read().splitlines()

# a capa = linhas iniciais até a 1ª em branco; depois a linha de "Roteiro calibrado..."
# tratamos linha a linha com regras simples.
def is_sep(s): return bool(re.fullmatch(r'_{5,}', s.strip()))
def is_slide_head(s): return bool(re.match(r'SLIDE\s', s.strip()))
def is_section_head(s): return s.strip() in ("Possíveis perguntas da professora",)
def is_question(s): return bool(re.match(r'\d+\.\s', s.strip()))
def is_answer(s): return s.strip().startswith("→")

# índice da primeira linha em branco (fim da capa)
first_blank = next((i for i,l in enumerate(lines) if l.strip()==""), len(lines))

i = 0
cover_done = False
while i < len(lines):
    raw = lines[i]
    s = raw.strip()
    if s == "":
        i += 1; continue

    # capa: até first_blank
    if i < first_blank:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(s)
        if i == 0:
            r.bold = True; r.font.size = Pt(15); r.font.color.rgb = SLATE
        elif i in (1,2):
            r.bold = True; r.font.size = Pt(12); r.font.color.rgb = SLATE
        else:
            r.font.size = Pt(11)
        i += 1; continue

    # linha "Roteiro calibrado ..." (subtítulo após capa)
    if s.startswith("Roteiro calibrado"):
        p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(s); r.italic = True; r.font.color.rgb = GREY; r.font.size = Pt(10.5)
        i += 1; continue

    if is_sep(s):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run("―"*48); r.font.color.rgb = RGBColor(0xcc,0xcc,0xcc)
        i += 1; continue

    if is_slide_head(s):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        r = p.add_run(s); r.bold = True; r.font.size = Pt(12.5); r.font.color.rgb = SLATE
        i += 1; continue

    if is_section_head(s):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        r = p.add_run(s); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = SLATE
        i += 1; continue

    if s.startswith("Dica:"):
        p = doc.add_paragraph()
        r = p.add_run(s); r.italic = True; r.font.color.rgb = GREY; r.font.size = Pt(10.5)
        i += 1; continue

    if is_question(s):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(6)
        r = p.add_run(s); r.bold = True
        i += 1; continue

    if is_answer(s):
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Pt(18)
        p.add_run(s)
        i += 1; continue

    # parágrafo normal (fala)
    p = doc.add_paragraph()
    p.add_run(s)
    i += 1

doc.save(OUT)
print("gerado:", OUT)
