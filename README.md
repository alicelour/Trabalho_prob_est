# Máquina Estatística: Probabilidade, Apostas e Pensamento Crítico

## 1. Sobre o projeto

O projeto **Máquina Estatística: Probabilidade, Apostas e Pensamento Crítico** consiste no desenvolvimento de um simulador de uma máquina de apostas, com o objetivo de aplicar conceitos de probabilidade e estatística em um cenário que permite analisar resultados aleatórios, ganhos, perdas e riscos financeiros.

A partir da simulação de partidas, será possível comparar probabilidades teóricas com frequências observadas, analisar o comportamento dos resultados ao longo de diferentes quantidades de rodadas e discutir criticamente questões sociais relacionadas aos jogos de azar.

## 2. Objetivos

### Objetivo geral

Compreender e aplicar conceitos probabilísticos e estatísticos por meio da construção e análise de um simulador de apostas, desenvolvendo também uma visão crítica sobre os riscos e as consequências sociais dos jogos de azar.

### Objetivos específicos

- Identificar o espaço amostral e os eventos associados ao funcionamento da máquina.
- Compreender a distribuição uniforme e a independência entre os rolos.
- Definir variáveis aleatórias discretas e suas respectivas distribuições de probabilidade.
- Calcular a esperança matemática do lucro e o retorno sobre os créditos apostados (RTP).
- Comparar probabilidades teóricas com frequências obtidas por simulação.
- Analisar média, mediana, desvio-padrão e variabilidade dos resultados.
- Investigar a Lei dos Grandes Números por meio de simulações de Monte Carlo.
- Avaliar probabilidades condicionais após resultados de prêmio e de perda.
- Discutir os limites das conclusões estatísticas e a relevância social do problema estudado.

## 3. Regras e funcionamento da máquina

A máquina é composta por três rolos independentes. Cada rolo possui cinco resultados possíveis, todos com a mesma probabilidade de ocorrência.

Como os três rolos são independentes, o espaço amostral possui:

\[
5^3 = 125
\]

Portanto, existem **125 combinações possíveis** para os três rolos.

Cada combinação específica possui probabilidade teórica de:

\[
P(\text{combinação}) =
\frac{1}{5}\times\frac{1}{5}\times\frac{1}{5}
=\frac{1}{125}=0{,}8\%
\]

Entre as 125 combinações, existem cinco triplas premiadas. Considerando que essas combinações são distintas e que somente elas concedem prêmio, a probabilidade teórica de obter um prêmio é:

\[
P(\text{prêmio})=\frac{5}{125}=4\%
\]

A probabilidade de não obter prêmio é:

\[
P(\text{sem prêmio})=\frac{120}{125}=96\%
\]

Os resultados de cada rodada são determinados aleatoriamente. Assim, as frequências observadas não são fixadas antecipadamente: elas são calculadas a partir dos resultados efetivamente obtidos nas simulações.

**Observação:** os valores pagos por cada tripla premiada e as demais regras financeiras devem seguir a tabela de pagamentos definida no enunciado do trabalho.

## 4. Conceitos matemáticos e estatísticos

### 4.1 Espaço amostral, eventos e contagem

O espaço amostral corresponde ao conjunto das 125 combinações possíveis dos três rolos. Os eventos de interesse incluem a ocorrência de uma das cinco triplas premiadas e o evento complementar, no qual não há prêmio.

### 4.2 Distribuição uniforme e independência

Cada rolo possui cinco resultados equiprováveis, com probabilidade de 20% para cada resultado. Como os rolos são independentes, as probabilidades de resultados específicos podem ser multiplicadas para determinar a probabilidade de uma combinação.

### 4.3 Variável aleatória discreta

O prêmio \(P\) representa o valor recebido em uma rodada, conforme a combinação obtida e a tabela de pagamentos.

O lucro \(X\) representa a diferença entre o valor recebido e o valor apostado:

\[
X=P-\text{aposta}
\]

É importante distinguir a variável aleatória, que representa os valores possíveis e suas probabilidades, do resultado efetivamente observado em uma rodada.

### 4.4 Esperança matemática e retorno sobre as apostas

A esperança matemática representa o valor médio esperado de uma variável aleatória ao longo de muitas repetições do experimento.

O retorno sobre os créditos apostados, conhecido como RTP (*Return to Player*), corresponde à razão entre o total esperado de pagamentos e o total apostado, expressa em porcentagem.

Essas medidas serão calculadas a partir das probabilidades dos resultados e da tabela de pagamentos, permitindo avaliar matematicamente o retorno esperado do jogo.

### 4.5 Frequências e estatística descritiva

Após as simulações, serão calculadas as frequências absolutas e relativas dos resultados, além de medidas como média, mediana e desvio-padrão.

Essas medidas permitirão descrever os resultados observados, identificar sua variabilidade e compará-los com os valores teóricos.

### 4.6 Lei dos Grandes Números e simulação de Monte Carlo

Serão realizadas simulações com diferentes quantidades de rodadas para comparar as médias acumuladas com a esperança matemática.

A análise permitirá observar como os resultados oscilam entre diferentes execuções e como as médias tendem a se aproximar do valor esperado à medida que o número de repetições aumenta, sem garantir igualdade em uma execução específica.

### 4.7 Probabilidade condicional

A probabilidade de obter prêmio após uma perda será comparada à probabilidade de obter prêmio após um prêmio anterior.

Como as rodadas são independentes, o resultado anterior não altera a probabilidade teórica da rodada seguinte. Eventuais diferenças nas frequências observadas podem ocorrer devido à variabilidade amostral.

### 4.8 Amostragem e limites da inferência

Os participantes virtuais e os resultados gerados pelo simulador constituem uma amostra de um modelo matemático. Eles não representam, por si só, o comportamento de uma população real de jogadores.

Por isso, as conclusões deverão considerar a incerteza, as limitações do modelo e a diferença entre associação estatística e causalidade.


## 5. Tecnologias utilizadas

- **Python:** implementação da lógica do simulador, geração de resultados aleatórios e cálculos estatísticos.
- **Git:** controle de versão do código-fonte.
- **GitHub:** armazenamento e colaboração no projeto.
- **Visual Studio Code:** ambiente de desenvolvimento.

## 6. Metodologia

O desenvolvimento será dividido nas seguintes etapas:

1. Definição do modelo probabilístico e do espaço amostral.
2. Implementação dos três rolos e das combinações premiadas.
3. Implementação da tabela de pagamentos e dos cálculos financeiros.
4. Execução de simulações com diferentes quantidades de rodadas.
5. Cálculo das frequências, medidas descritivas, esperança matemática e RTP.
6. Comparação entre resultados teóricos e observados.
7. Análise crítica dos resultados e elaboração das conclusões.

## 7. Integrantes

- Alice Lourenço dos Reis
- Davi Sutil
- Karyna Carbas
- Remerson Victor Silva da Assurreição

## 9. Considerações finais

O projeto busca integrar programação, probabilidade, estatística e reflexão social em um experimento computacional. Ao comparar o modelo teórico com os resultados observados, pretende-se compreender melhor a aleatoriedade, a variabilidade amostral e os limites das conclusões obtidas a partir de simulações.
