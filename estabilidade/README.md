# Parte 2 — Estabilidade (João)

Slides da parte de **estabilidade / linearização** do Projeto 2 de EDO, no mesmo estilo
visual do deck da Camilla (feito no Canva). Esta pasta é **independente**: nada do deck da
Camilla foi alterado. A ideia é apresentar esta sequência logo após o slide "Estabilidade"
(fundo azul/cinza) que já existe no deck dela.

## Arquivos

| Arquivo | O que é |
|---|---|
| **`Estabilidade_Joao_canva.pdf`** | **Versão para IMPORTAR NO CANVA mantendo o texto editável.** O texto continua texto (você muda tamanho/palavras); cada **equação é uma imagem** que o Canva não quebra e que você redimensiona (arrastar os cantos = aumentar a "fonte" da conta). **É o recomendado para editar no Canva.** |
| `Estabilidade_Joao_imagens.pdf` | Cada slide como uma imagem única. Importa 100% limpo, mas **nada é editável** (nem texto). Use se só for apresentar/montar sem editar. |
| `slides_png/` | Cada slide como PNG individual (3200×1800). Alternativa: arraste como fundo de página no Canva. |
| `Estabilidade_Joao.pdf` | Slides com equações vetoriais (KaTeX). Ótimo para apresentar direto do PDF, mas **não importe no Canva** — lá as equações viram centenas de fragmentos embaralhados. |
| `slides.html` | Fonte editável dos slides (HTML + CSS + KaTeX). |
| `estilo.css` | Template visual (cores, fontes, rodapé) replicando o Canva da Camilla. |
| `roteiro_fala.md` | Roteiro de fala slide a slide, com tempos (~30 min) e perguntas prováveis. |
| `gerar_figuras.py` | Gera as 4 figuras (planos de fase e potenciais) com matplotlib. |
| `figuras/` | PNGs das figuras usadas nos slides. |
| `fonts/` | Poppins + Open Sans (woff2) embutidos — mesma fonte do deck. |
| `katex/` | KaTeX local (CSS, JS e fontes) para renderizar as equações offline. |

## Conteúdo dos slides

1. Estabilidade (divisor de seção)
2. O que vamos responder (roteiro)
3. Da 2ª ordem para um sistema de 1ª ordem
4. Pontos de equilíbrio — único em (0,0)
5. Parte linear × parte não linear (série binomial)
6. O sistema homogêneo `Y' = JY`
7. Autovalores `λ = ±iω` (h > 0)
8. Solução e retrato de fase: **centro**
9. A linearização sozinha basta? (caso não hiperbólico)
10. O termo **α** — por que o centro pode virar espiral
11. **Energia** decide (função de Lyapunov, h > 0)
12. Linear × não linear (figura comparando planos de fase)
13. O potencial confirma (figura)
14. O caso degenerado **h = 0** (parte 1)
15. h = 0: o não linear manda (parte 2)
16. Formulação final (tabela-resumo)
17. Obrigado / dúvidas

## Importar no Canva (sem os erros de antes)

**Por que o PDF original dava erro no Canva:** as equações eram texto vetorial (LaTeX/KaTeX).
O Canva não entende matemática, então ao importar ele quebrava cada equação em dezenas de
glifos soltos, com frações, raízes e acentos embaralhados.

**Solução — importe `Estabilidade_Joao_canva.pdf`:**
- O **texto** (títulos, parágrafos, bullets, rodapé) entra como **texto editável** no Canva —
  você muda tamanho e palavras normalmente.
- Cada **equação** entra como **imagem** (PNG transparente). O Canva não quebra imagem.
  Para "mudar o tamanho da fonte" de uma conta, basta **selecionar a imagem e arrastar o canto**.

As equações ficam na pasta `eq_img/` (uma por arquivo). Se quiser trocar alguma por uma maior,
me peça e eu regero, ou rode `gerar_equacoes.py` e `montar_canva.py`.

### Como regerar a versão Canva
```bash
python3 gerar_equacoes.py        # gera eq_img/*.png (equações) + eq_map.json
python3 montar_canva.py          # gera slides_canva.html
chrome --headless --no-sandbox --disable-gpu --no-pdf-header-footer \
  --virtual-time-budget=8000 --run-all-compositor-stages-before-draw \
  --print-to-pdf=Estabilidade_Joao_canva.pdf slides_canva.html
```

## Como editar e regerar o PDF

1. Edite `slides.html` (texto) e/ou `gerar_figuras.py` (gráficos).
2. Se mexeu nas figuras, regere-as:
   ```bash
   python3 gerar_figuras.py            # requer numpy + matplotlib
   ```
3. Regere o PDF com o Chrome headless:
   ```bash
   chrome --headless --no-sandbox --disable-gpu --no-pdf-header-footer \
     --virtual-time-budget=8000 --run-all-compositor-stages-before-draw \
     --print-to-pdf=Estabilidade_Joao.pdf slides.html
   ```
   (Qualquer navegador baseado em Chromium serve. Alternativa manual: abrir `slides.html`
   no navegador e usar Imprimir → Salvar como PDF, com margens zero e tamanho 1280×720.)

## Parâmetros usados nas figuras

`L = k = m = 1` (os mesmos do item 2c da Camilla). O alongamento `h` varia conforme o
slide (h = 0,5 nos planos de fase; h ∈ {1; 0,5; 0,1; 0} no potencial).

## Observação encontrada no material (opcional, confira com a Camilla)

No **slide 7** do deck dela, a figura/texto traz `cos α = x/(L+h)`; o correto é
`cos α = x / sqrt((L+h)² + x²)` — é justamente essa fração que gera o fator
`1 − L/sqrt(...)` na equação da força. No desenvolvimento manuscrito está certo; parece ser
só um erro de digitação no slide. Não alterei nada no deck dela; fica a sugestão.
