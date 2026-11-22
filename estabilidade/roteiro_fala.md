# Roteiro de fala — Parte 2: Estabilidade (João)

Tempo-alvo: ~30 min. A parte começa logo após o slide "Estabilidade" (fundo azul/cinza)
do deck da Camilla. Os tempos são sugestões; ajuste no ensaio.

> Dica geral: a professora pediu três coisas — (1) abrir a linearização num **sistema
> homogêneo**, (2) achar os **autovalores**, (3) decidir se a **parte não linear** se
> ajusta ou se pode ser eliminada. Volte a esses três verbos ao longo da fala.

---

## S1 — "Estabilidade" (divisor de seção) — 15 s
Transição: "A Camilla mostrou a linearização e a frequência natural. Agora eu assumo e
pergunto: esse modelo linear descreve mesmo a estabilidade do sistema? É o que vamos
investigar."

## S2 — O que vamos responder — 1 min
Apresente o roteiro. Leia a "pergunta central" e conecte com as falas da professora
(sistema homogêneo, autovalores, ajustar/eliminar a não-linearidade).

## S3 — Da 2ª ordem para um sistema — 3 min
- Retome `f(x)` da Camilla.
- Introduza as variáveis de estado `y1 = x`, `y2 = x'`.
- Mostre que a EDO de 2ª ordem vira um sistema de 1ª ordem.
- Frase-chave: "toda a análise de estabilidade acontece no plano de fases (x, x')".

## S4 — Pontos de equilíbrio — 2 min
- Equilíbrio = nada varia: `y1' = y2' = 0`.
- Argumento da raiz: `sqrt(a²+x²) ≥ a ≥ L`, então a fração ≤ 1, com igualdade só se x=0.
- Conclusão: único equilíbrio em (0,0) — o ponto em torno do qual se linearizou.

## S5 — Parte linear × parte não linear — 4 min
- Série binomial de `(1+u)^(-1/2)`: aparece o termo linear `(2kh/a)x` e o cúbico `(kL/a³)x³`.
- Destaque: coeficientes batem com os da Camilla (slide 16); não há termo em x² porque f é ímpar.
- Defina `ω² = f'(0)/m` e escreva o sistema como **parte linear J·Y + parte não linear G(Y)**.

## S6 — O sistema homogêneo — 4 min
- `||G(Y)||/||Y|| → 0`: perto da origem a não-linearidade é desprezível.
- Essa é a "parte não linear" da professora. Tirando-a, sobra `Y' = JY`.
- Enfatize: é **homogêneo** (sem termo independente) e de coeficientes constantes — exatamente
  o que a professora pediu para escrever.

## S7 — Autovalores (h > 0) — 2 min
- `det(J - λI) = λ² + ω² = 0` ⇒ `λ = ±iω`.
- Imaginários puros. Autovetor `v = (1, iω)`.

## S8 — Solução e retrato de fase: centro — 3 min
- Solução geral com seno/cosseno; Wronskiano `W = ω ≠ 0` (reproduz o slide 14 da Camilla).
- Órbitas são elipses: `ω²y1² + y2² = const`.
- Classificação: Re λ = 0 ⇒ **centro** (estável, mas não assintoticamente).

## S9 — A linearização sozinha basta? — 3 min
- Teorema da linearização (Hartman–Grobman) só vale para equilíbrio **hiperbólico** (Re λ ≠ 0).
- Aqui Re λ = 0 ⇒ não hiperbólico ⇒ o teorema **não decide**. Prepare o exemplo do α.

## S10 — O termo α (por que o centro pode mentir) — 3 min
- Sistema com a mesma parte linear (±i) + perturbação cúbica αx(x²+y²).
- Em polares: `r' = α r³`, `θ' = 1`.
- α<0 espiral estável, α>0 espiral instável, α=0 centro. **Mesma linearização, três destinos.**
- Moral: precisamos de outra ferramenta → a energia.

## S11 — Energia decide (h > 0) — 5 min
- Potencial `V(x) = ∫f`, energia `E = ½mv² + V`.
- `dE/dt = v(mx'' + f) = 0`: energia conservada.
- `V(0)=0`, `V'(0)=0`, `V''(0)=f'(0)>0` (h>0) ⇒ mínimo estrito ⇒ E definida positiva.
- E é função de Lyapunov conservada ⇒ curvas E=c fechadas ⇒ o não-linear **também é um centro**.

## S12 — Linear × não linear (figura) — 2 min
- Mostre as elipses (esquerda) vs. órbitas não lineares (direita): qualitativamente iguais.
- O que se perde ao eliminar a não-linearidade é só quantitativo: o cúbico positivo faz a
  mola "endurecer"; a frequência real cresce com a amplitude (conecta com o item d da Camilla).

## S13 — O potencial confirma — 1-2 min
- V(x) (laranja) vs. aproximação quadrática (azul) para vários h.
- Perto de x=0 coincidem (linearização boa localmente); com h→0 o poço quadrático some.

## S14 — O caso degenerado h = 0 (parte 1) — 2-3 min
- ω = 0 ⇒ J nilpotente, λ=0 duplo com um só autovetor.
- Solução linear `y1 = y1(0) + y2(0)t`: cresce sem limite; todo (c,0) vira equilíbrio do linear.
- O modelo linear perde a dinâmica.

## S15 — h = 0: o não linear manda (parte 2) — 2-3 min
- Equação relevante: `mx'' + (k/L²)x³ = 0`; energia `≈ kx⁴/(4L²)`, definida positiva ⇒ órbitas
  fechadas, estável e periódico.
- Período ∝ 1/A: **não existe** frequência natural fixa.
- Resposta direta: h>0 **dá para eliminar** (só quantitativo); h=0 **não dá** (destrói a força).
  Fecha com o item (e) da Camilla.

## S16 — Formulação final (tabela) — 1-2 min
- Leia a tabela: autovalores, linearização, não-linear, pode eliminar? — para h>0 e h=0.
- Amarre os três verbos da professora.

## S17 — Obrigado / dúvidas — 15 s

---

### Possíveis perguntas da professora (prepare-se)
- "Por que o centro é só estável e não assintoticamente estável?" → não há dissipação; energia
  conservada, órbitas fechadas, a solução não tende ao equilíbrio.
- "A linearização está errada então?" → não; ela é correta **localmente** e para h>0 dá o quadro
  qualitativo certo. O cuidado é que, sendo o equilíbrio não hiperbólico, foi a **energia** (não o
  teorema da linearização) que garantiu a conclusão.
- "O que muda fisicamente de h>0 para h=0?" → com h>0 há pré-tensão nas molas e surge uma força
  restauradora linear (frequência bem definida). Com h=0 a força restauradora é puramente cúbica:
  sem rigidez linear, sem frequência natural fixa.
