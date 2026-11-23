Roteiro Falado — Seminário (substitui a Prova 2)
Equações Diferenciais Ordinárias · Projeto 2 — Parte de Estabilidade e Linearização
Linearização de um Sistema Mecânico Não Linear — duas molas (Brannan & Boyce)
João Gabriel de Souza Zamboni — RA 178164

Roteiro calibrado para ~30 minutos de fala. A minha parte começa logo após o slide "Estabilidade" (fundo azul/cinza) do deck, depois da parte da Camilla. Os tempos são aproximados e deixam margem para pausas.
____________________________________________________________

SLIDE 1 — "Estabilidade" (divisor de seção)   (~0:20)
Boa tarde a todos. Eu sou o João Gabriel. A Camilla acabou de mostrar a linearização do sistema das duas molas, achou a equação linearizada e a frequência natural. A partir daqui eu assumo, e a pergunta que eu quero responder é a seguinte: tudo bem, a gente linearizou — mas será que esse modelo linear descreve mesmo a estabilidade do sistema de verdade? É isso que eu vou investigar nesta segunda parte.

SLIDE 2 — Estabilidade: o que vamos responder   (~1:30)
Antes de entrar nas contas, deixa eu dizer para onde a gente vai, porque isso segue exatamente o que a professora pediu. Ela pediu três coisas, e eu vou passar por elas nessa ordem.
Primeiro: pegar a linearização e abrir ela num sistema — e tem que ser um sistema homogêneo. Segundo: achar os autovalores desse sistema. E terceiro: olhar a parte não linear e decidir se dá para ajustar, ou se a gente pode simplesmente eliminar essa parte.
Então o meu roteiro é esse. Eu vou: transformar a equação de segunda ordem num sistema de primeira ordem e achar o equilíbrio; separar a parte linear da não linear e montar o sistema homogêneo; calcular os autovalores e o retrato de fase; mostrar por que, nesse caso, a linearização sozinha não decide; e aí usar a energia para fechar a conclusão — inclusive no caso especial em que o alongamento h é zero.
Dica: Leia a "pergunta central" da caixa em voz alta e conecte com as três falas da professora. É o fio condutor da sua parte inteira.

SLIDE 3 — Da 2ª ordem para um sistema   (~3:00)
Então vamos começar. A Camilla deixou a gente com a equação de movimento: m x duas linhas, mais f de x, igual a zero — onde f de x é aquela força restauradora das molas, com a raiz de (L+h) ao quadrado mais x ao quadrado no denominador. Para encurtar a notação, eu vou chamar L mais h de "a".
O problema é que essa é uma equação de segunda ordem, e para estudar estabilidade é muito mais natural trabalhar com um sistema de primeira ordem. Então eu faço a troca padrão: chamo a posição de y1, que é o próprio x, e chamo a velocidade de y2, que é x linha.
Com isso, aquela equação única de segunda ordem vira um par de equações de primeira ordem: y1 linha é igual a y2 — ou seja, a derivada da posição é a velocidade —, e y2 linha é igual a menos um sobre m vezes f de y1 — que é a aceleração, vinda da segunda lei de Newton.
O ponto que eu quero que fique é este: a partir de agora, toda a análise acontece nesse plano de estados (x, x linha), que a gente chama de plano de fases. Cada ponto desse plano é uma posição e uma velocidade; e uma solução do sistema é uma curva andando nesse plano.
Dica: Vá devagar aqui. Se a banca entender que y1 é posição e y2 é velocidade, todo o resto flui. Aponte para o sistema na caixa enquanto fala.

SLIDE 4 — Pontos de equilíbrio   (~2:00)
A primeira coisa a fazer com um sistema desses é achar os equilíbrios — os pontos onde nada se mexe, ou seja, onde as duas derivadas são zero.
Para y1 linha ser zero, eu preciso de y2 igual a zero: velocidade nula. E para y2 linha ser zero, eu preciso de f de y1 igual a zero: força nula.
Aí entra um argumento geométrico simples. A raiz de a ao quadrado mais x ao quadrado é sempre maior ou igual a "a", que por sua vez é maior ou igual a L. Isso faz aquela fração L sobre a raiz ser sempre menor ou igual a 1 — e só dá exatamente 1 quando x é zero. Logo, f de x só zera quando x é zero.
Conclusão: o único equilíbrio do sistema é a origem, o ponto (0,0) — posição central, parado. E repare que é exatamente o ponto em torno do qual a Camilla linearizou. Então a gente está, de fato, estudando a estabilidade do ponto certo.

SLIDE 5 — Parte linear × parte não linear   (~4:00)
Agora o passo que a professora chamou de "tirar a não linearidade". A ideia é escrever a força f como a parte linear mais um resto: f de x igual a f linha de zero vezes x, mais r de x, onde esse r junta tudo que não é linear.
Para achar esses pedaços, eu expando a força numa série — é a série binomial de (1 mais u) elevado a menos um meio, com u sendo x ao quadrado sobre a ao quadrado. Fazendo as contas, aparece um termo linear, com coeficiente 2kh sobre a, e o primeiro termo não linear é cúbico, com coeficiente kL sobre a ao cubo.
Dois detalhes que valem comentar. Primeiro: esses coeficientes batem exatamente com os que a Camilla encontrou no polinômio de Taylor dela, lá no slide 16 — então as duas abordagens conversam. Segundo: não existe termo em x ao quadrado. E isso não é coincidência: a força f é uma função ímpar, então os termos de grau par somem. Por isso o resto r começa só no grau três.
Agora eu defino a frequência ao quadrado, ômega ao quadrado, como f linha de zero sobre m — que dá 2kh sobre m vezes (L mais h). Com isso, eu consigo escrever o sistema inteiro de um jeito muito claro: uma parte linear, que é a matriz J vezes o vetor Y, mais uma parte não linear, que eu chamo de G de Y, e que carrega só aquele resto cúbico.
Dica: Não precisa deduzir a série binomial no quadro. Diga "expandindo em série, aparece o termo linear e o primeiro corretor cúbico" e foque em: os coeficientes batem com os da Camilla, e não há termo quadrático porque f é ímpar.

SLIDE 6 — O sistema homogêneo   (~4:00)
Aqui está o pulo do gato, e é literalmente o que a professora pediu: montar o sistema homogêneo.
Olha o que acontece perto da origem. Como o resto r é de ordem cúbica, ele é muito pequeno comparado com o termo linear quando a gente está perto de zero. Formalmente: a norma de G de Y dividida pela norma de Y tende a zero quando Y tende a zero. Em palavras: pertinho do equilíbrio, a parte não linear é desprezível frente à linear.
Essa parte não linear é exatamente a "não linearidade" que a professora falou em tirar. E quando eu removo ela, o que sobra é o sistema linear homogêneo: Y linha igual a J Y, com aquela matriz J de duas por duas.
Eu quero enfatizar duas palavras aqui, porque elas eram o pedido explícito. É homogêneo — o lado direito só depende de Y, não tem nenhum termo solto, constante. E é de coeficientes constantes — a matriz J não muda com o tempo. Ou seja, é exatamente o tipo de sistema para o qual a gente sabe aplicar o método dos autovalores. Que é o próximo passo.

SLIDE 7 — Autovalores (h maior que zero)   (~2:00)
Então vamos aos autovalores, por enquanto no caso em que o alongamento h é positivo. O método é o padrão: eu procuro os lambdas que anulam o determinante de J menos lambda vezes a identidade.
Montando esse determinante para a nossa matriz, dá uma equação bem limpa: lambda ao quadrado mais ômega ao quadrado igual a zero. Resolvendo, lambda é igual a mais ou menos i ômega.
Ou seja: os autovalores são imaginários puros — não têm parte real, só parte imaginária. Guardem isso, porque é justamente esse detalhe que vai tornar a análise interessante daqui a pouco. E o autovetor associado, para quem quiser conferir, é o vetor (1, i ômega).

SLIDE 8 — Solução e retrato de fase: um centro   (~3:00)
Com autovalores imaginários puros, a solução geral do sistema homogêneo é uma combinação de senos e cossenos de ômega t — eu mostrei a fórmula completa no slide. Para garantir que são de fato duas soluções independentes, dá para checar o Wronskiano, que vale ômega e é diferente de zero. Isso, aliás, reproduz o cálculo do Wronskiano que a Camilla fez no slide 14 dela.
E qual é o formato dessas órbitas no plano de fases? Se eu olhar a combinação ômega ao quadrado y1 ao quadrado mais y2 ao quadrado, a derivada dela no tempo é zero — ou seja, essa quantidade se conserva. E isso é a equação de uma elipse. Então as trajetórias são elipses fechadas em volta da origem, como está no desenho à direita.
Isso define o tipo do equilíbrio: como os autovalores têm parte real zero, a origem é um centro. Centro quer dizer estável — as soluções ficam girando em volta, não explodem —, mas não assintoticamente estável, porque elas também não decaem para o equilíbrio; ficam circulando para sempre.
Dica: Mostre o desenho das elipses enquanto fala "órbitas fechadas". A diferença entre "estável" e "assintoticamente estável" costuma virar pergunta — deixe clara aqui.

SLIDE 9 — A linearização sozinha basta?   (~3:00)
Agora o ponto delicado, e é aqui que a parte de estabilidade fica interessante de verdade. Existe um teorema, o teorema da linearização — também conhecido como Hartman-Grobman — que diz quando o retrato de fase do sistema não linear se parece com o do linear. Mas ele tem uma condição: o equilíbrio precisa ser hiperbólico, ou seja, os autovalores precisam ter parte real diferente de zero.
E qual é o nosso caso? Os nossos autovalores são mais ou menos i ômega, com parte real igual a zero. Então o equilíbrio não é hiperbólico, e o teorema simplesmente não se aplica. Em outras palavras: só com a linearização, eu não posso afirmar a estabilidade do sistema real. A linearização, sozinha, não decide.
Por que esse cuidado todo? Porque, quando a parte real é zero, aquela parte não linear que a gente jogou fora — por menor que ela pareça — pode mudar o resultado. Ela pode transformar um centro numa espiral. E para mostrar que isso não é conversa, eu trouxe o exemplo clássico no próximo slide.

SLIDE 10 — Por que o centro pode mentir: o termo alfa   (~3:00)
Esse é o exemplo que fecha o argumento. Imagina um sistema que tem exatamente a mesma parte linear do nosso — um centro, autovalores mais ou menos i — mas com uma perturbação não linear pequena, controlada por um parâmetro que eu vou chamar de alfa. Está escrito no slide: x linha e y linha, com um termo alfa vezes x, ou y, vezes (x ao quadrado mais y ao quadrado).
Se eu só olhasse a parte linear, concluiria "é um centro, estável" e pararia por aí. Mas vamos passar para coordenadas polares, com r sendo a distância até a origem. Aí o sistema fica lindo: r linha é igual a alfa vezes r ao cubo, e o ângulo gira com velocidade constante.
E agora olha o que o sinal do alfa faz. Se alfa é negativo, o r diminui com o tempo: a trajetória espirala para dentro, é uma espiral estável, que atrai. Se alfa é positivo, o r cresce: espiral instável, que repele. E só se alfa for exatamente zero é que a gente tem o centro de verdade.
A moral é essa: três sistemas com comportamentos completamente diferentes — atrai, repele, ou fica girando — têm todos a mesma linearização. Por isso a linearização, sozinha, não consegue distinguir. A gente precisa de outra ferramenta. E essa ferramenta é a energia.
Dica: Esse é o slide que justifica todo o resto. Enfatize o "mesma linearização, três destinos diferentes". As três caixinhas coloridas ajudam a fixar: azul atrai, laranja repele, neutro gira.

SLIDE 11 — A energia decide (h maior que zero)   (~5:00)
Então vamos de energia. Para um sistema mecânico como o nosso, isso é natural. Eu defino o potencial V de x como a integral da força — que dá aquela expressão com a raiz —, e a energia total E como a energia cinética, um meio m v ao quadrado, mais o potencial.
E aí vem o fato-chave: ao longo de qualquer solução do sistema, a energia E é conservada. A conta é direta: a derivada de E no tempo dá v vezes (m x duas linhas mais f de x), e isso é zero, porque é exatamente a equação de movimento. Ou seja, dE/dt igual a zero — a energia não muda.
Agora eu preciso mostrar que esse potencial tem um mínimo de verdade na origem. Três checagens: V de zero é zero; a derivada V linha de zero é zero — ponto crítico; e a segunda derivada V duas linhas de zero é igual a f linha de zero, que é 2kh sobre a, e isso é positivo quando h é maior que zero. As três juntas dizem que o potencial tem um mínimo estrito na origem. E isso faz a energia ser uma função definida positiva em volta do equilíbrio.
Com isso eu fecho o argumento: a energia é uma função de Lyapunov conservada. As curvas de energia constante são fechadas em torno da origem, exatamente as órbitas do movimento. Então o sistema não linear também é um centro — estável, com todas as soluções periódicas. E repare: isso eu provei com a energia, não com a linearização. Foi a energia que decidiu o que a linearização não podia.
Dica: Este é o slide mais denso. Vá com calma nas três checagens do potencial. Se a banca entender "energia conservada mais mínimo estrito igual a órbitas fechadas", a conclusão vem sozinha.

SLIDE 12 — Linear × não linear: dá para eliminar?   (~2:00)
E aqui está a resposta visual para a pergunta da professora: "dá para eliminar a parte não linear?". Este gráfico tem dois painéis, os dois com h igual a 0,5. À esquerda, as elipses do sistema linearizado; à direita, as órbitas do sistema não linear completo.
Comparando os dois, a resposta salta aos olhos: eles são qualitativamente iguais. Os dois têm um centro, os dois têm órbitas fechadas em volta da origem. A diferença é só de forma: as órbitas do não linear estão levemente deformadas.
Então, para h maior que zero: sim, dá para eliminar a parte não linear sem mudar o quadro qualitativo. O que a gente perde ao eliminar é só quantitativo. Como o coeficiente cúbico é positivo, a mola "endurece" conforme a amplitude cresce, e a frequência real sobe um pouco com a amplitude. Isso, aliás, conversa direto com o item (d) que a Camilla apresentou.

SLIDE 13 — O potencial confirma   (~1:30)
Esse slide é um reforço visual, com o potencial. A curva laranja é o potencial não linear de verdade; a azul tracejada é a aproximação quadrática, que corresponde ao modelo linear. Eu plotei para vários valores de h.
Duas leituras. Primeira: para h maior que zero, o potencial é um poço com fundo bem definido — mínimo estrito — e é isso que garante as órbitas fechadas e o centro estável. Segunda: pertinho de x igual a zero, as duas curvas praticamente se colam, o que confirma que a linearização é boa localmente, para pequenas oscilações. E repare que, conforme o h vai diminuindo para zero, o poço quadrático vai ficando mais raso — quase plano. Isso já anuncia o problema do próximo caso.

SLIDE 14 — O caso degenerado h = 0 (parte 1)   (~2:30)
Agora o caso especial: h igual a zero, sem alongamento inicial. Aqui a coisa muda de figura. Com h zero, o ômega vai a zero, e a parte linear colapsa. A matriz J vira um bloco nilpotente, e o autovalor é lambda igual a zero, duplo, com um único autovetor.
E o que o modelo linearizado prevê nesse caso? A solução dele é y1 igual a y1 de zero mais y2 de zero vezes t — ou seja, uma reta, que cresce sem limite se a velocidade inicial não for zero. Pior ainda: no sistema linear, todo ponto da forma (c, 0) vira um equilíbrio — qualquer posição parada seria um equilíbrio. Mas no sistema original, a gente já viu que o único equilíbrio é a origem.
Então, nesse caso, o modelo linear não só é impreciso: ele perde completamente a dinâmica. Ele inventa equilíbrios que não existem e prevê que a massa escapa, quando na verdade ela oscila.

SLIDE 15 — h = 0: o não linear manda (parte 2)   (~2:30)
Por que o modelo linear erra tão feio com h igual a zero? Porque, nesse caso, a parte não linear é justamente a que manda. Quando o termo linear some, quem sobra como força restauradora é o termo cúbico. A equação que realmente governa o movimento é m x duas linhas mais k sobre L ao quadrado, vezes x ao cubo, igual a zero.
E essa equação tem uma energia bem comportada: o potencial fica proporcional a x à quarta, que é definido positivo. Então, de novo, a gente tem órbitas fechadas — o sistema é estável e periódico, como se vê no painel da direita do gráfico. O painel da esquerda mostra o modelo linear, com aquelas retas horizontais que não oscilam: completamente diferente.
Tem um detalhe bonito aqui: por um argumento de escala, o período dessas oscilações é proporcional a 1 sobre a amplitude. Ou seja, não existe uma frequência natural fixa — a frequência depende de quão longe você solta a massa. Isso responde diretamente ao que a professora perguntou, sobre ajustar ou eliminar: para h maior que zero, dá para eliminar a parte não linear; para h igual a zero, não dá de jeito nenhum — eliminar ela destrói a força restauradora. E isso fecha com o item (e) da Camilla.
Dica: Contraste os dois painéis do gráfico com o dedo: "à esquerda o linear, retas que não voltam; à direita o real, órbitas fechadas". É a imagem que prova que o não linear manda.

SLIDE 16 — Formulação final   (~1:30)
Esse slide é o resumo de tudo, numa tabela, comparando os dois casos: h maior que zero e h igual a zero.
Autovalores: no primeiro caso, mais ou menos i ômega; no segundo, lambda zero duplo, nilpotente. Linearização: no primeiro caso, dá um centro, estável; no segundo, dá uma coisa degenerada, instável, que não serve. Sistema não linear de verdade: nos dois casos é estável — centro no primeiro, periódico no segundo —, e isso quem garantiu foi a energia. E a última linha é a resposta à professora: dá para eliminar a parte não linear? Para h maior que zero, sim, qualitativamente; para h igual a zero, não.
Amarrando com os três pedidos dela: eu abri a linearização num sistema homogêneo, calculei os autovalores, e decidi sobre a parte não linear — com a energia entrando em cena justamente onde a linearização não bastava.

SLIDE 17 — Obrigado / dúvidas   (~0:20)
E era isso. Muito obrigado pela atenção, e fico à disposição para as perguntas sobre a parte de estabilidade.

____________________________________________________________
Possíveis perguntas da professora

1. Por que o centro é só estável e não assintoticamente estável?
→ Porque não há dissipação no sistema — nenhum atrito. A energia é conservada, então as órbitas são fechadas e a solução fica circulando para sempre, sem tender ao equilíbrio. Assintoticamente estável exigiria que as trajetórias convergissem para a origem, e isso só acontece se houver perda de energia.

2. Então a linearização da Camilla está errada?
→ Não, de forma alguma. Ela está correta localmente, e para h maior que zero ela dá o quadro qualitativo certo: um centro, órbitas fechadas. O único cuidado é que, como o equilíbrio é não hiperbólico (parte real zero), quem garante a conclusão rigorosamente é a energia, e não o teorema da linearização. A linearização acerta, mas não é ela quem prova.

3. O que é um equilíbrio hiperbólico, e por que isso importa aqui?
→ É um equilíbrio cujos autovalores têm parte real diferente de zero. Quando isso vale, o teorema da linearização garante que o sistema não linear se comporta como o linear perto do equilíbrio. No nosso caso a parte real é zero, então estamos no caso de fronteira, onde o teorema não decide — e por isso precisei da energia.

4. Por que você usou a energia e não só os autovalores?
→ Porque os autovalores imaginários puros deixam o caso indefinido: um centro linear pode virar espiral estável ou instável sob perturbação não linear — foi o que mostrei no exemplo do alfa. A energia resolve isso diretamente: sendo conservada e tendo mínimo estrito na origem, ela é uma função de Lyapunov que prova as órbitas fechadas.

5. O que muda fisicamente de h maior que zero para h igual a zero?
→ Com h maior que zero, as molas estão pré-esticadas, e isso cria uma força restauradora linear — surge uma rigidez e uma frequência natural bem definida. Com h igual a zero não há pré-tensão: a força restauradora é puramente cúbica. Sem rigidez linear, não existe frequência natural fixa, e o período passa a depender da amplitude.

6. No caso h = 0, o sistema é estável ou não?
→ O sistema real é estável e periódico — a energia proporcional a x à quarta garante órbitas fechadas. Quem é instável e sem sentido é o modelo linearizado, que prevê a massa escapando e inventa uma linha inteira de equilíbrios falsos. É o exemplo mais claro de quando não se pode eliminar a parte não linear.

7. De onde vem o termo cúbico, e por que não há termo quadrático?
→ Os dois vêm da expansão em série da força f. Não há termo quadrático porque f é uma função ímpar — simétrica em relação à origem —, então todos os termos de grau par se anulam. O primeiro termo não linear que sobra é o cúbico, com coeficiente kL sobre a ao cubo.
