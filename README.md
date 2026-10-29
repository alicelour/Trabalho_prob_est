# 🎰 Máquina Estatística: Probabilidade, Apostas e Pensamento Crítico

Projeto desenvolvido para a disciplina de **Probabilidade e Estatística I**, do curso de Bacharelado em Sistemas de Informação do Instituto Federal do Espírito Santo (IFES) — Campus Serra.

O projeto consiste no desenvolvimento de um simulador de uma máquina de três rolos, com o objetivo de aplicar conceitos de probabilidade, variáveis aleatórias, valor esperado, estatística descritiva, simulação de Monte Carlo e probabilidade condicional.

> **Simulador acadêmico — somente créditos fictícios.**

## 👥 Integrantes

- Alice Lourenço dos Reis
- Remerson Victor Silva da Assurreição

## 🎯 Objetivos

- Implementar um simulador de uma máquina de três rolos com resultados aleatórios.
- Calcular probabilidades e valores esperados teoricamente.
- Comparar os resultados teóricos com os resultados observados nas simulações.
- Analisar a variação dos lucros e o comportamento das médias acumuladas.
- Investigar a independência entre rodadas e a probabilidade condicional.
- Avaliar como alterações nos pagamentos influenciam o retorno esperado.
- Exportar resultados em arquivos CSV e gerar gráficos para apoiar a análise.

## 🎮 Como funciona a máquina?

A máquina possui três rolos independentes, cada um com cinco símbolos organizados em uma sequência circular:

`A → B → C → D → E → A`

Cada rolo apresenta três símbolos consecutivos. Entretanto, **somente o símbolo central de cada rolo é utilizado para determinar o resultado da rodada**.

Cada posição central possui a mesma probabilidade de ser sorteada. Como existem cinco possibilidades por rolo, o espaço amostral contém:

\[
5^3 = 125 \text{ combinações}
\]

O jogador utiliza uma aposta fixa de 1 crédito fictício por rodada. Há prêmio somente quando os três símbolos centrais são iguais.

### Tabela de pagamentos

| Resultado | Prêmio bruto | Lucro líquido |
|---|---:|---:|
| A-A-A | 5 créditos | +4 créditos |
| B-B-B | 10 créditos | +9 créditos |
| C-C-C | 15 créditos | +14 créditos |
| D-D-D | 25 créditos | +24 créditos |
| E-E-E | 50 créditos | +49 créditos |
| Demais combinações | 0 crédito | −1 crédito |

O prêmio bruto corresponde ao valor recebido pela combinação premiada. O lucro líquido considera o custo da rodada:

\[
\text{Lucro líquido}=\text{Prêmio bruto}-\text{Aposta}
\]

## 📐 Fundamentação matemática

### Probabilidade de ganhar

Existem cinco combinações premiadas entre as 125 combinações possíveis:

\[
P(\text{ganhar})=\frac{5}{125}=4\%
\]

Consequentemente:

\[
P(\text{não ganhar})=\frac{120}{125}=96\%
\]

Cada combinação premiada individual possui probabilidade de \(1/125=0{,}8\%\).

### Valor esperado

O valor esperado do prêmio bruto é:

\[
E(P)=\frac{5+10+15+25+50}{125}=0{,}84
\]

Como cada rodada custa 1 crédito, o lucro líquido esperado é:

\[
E(X)=0{,}84-1=-0{,}16
\]

Portanto, o modelo possui uma perda líquida esperada de 0,16 crédito por rodada.

### Return to Player (RTP)

O RTP (*Return to Player*) representa a proporção dos créditos apostados que retorna ao jogador na forma de prêmios brutos.

\[
RTP=\frac{E(P)}{\text{Aposta}}\times100\%=84\%
\]

O RTP teórico é de 84%. Esse indicador não representa a probabilidade de ganhar, que é de 4%.

### Resultados teóricos e observados

Os valores teóricos são calculados matematicamente a partir das regras da máquina. Os valores observados são obtidos a partir dos resultados efetivamente gerados pelo simulador.

Como a simulação utiliza uma quantidade finita de rodadas, as frequências, as médias e o RTP observados podem diferir dos valores teóricos.

## 🧪 Experimentos realizados

### Experimento 1 — Distribuição dos resultados

Simula 10.000 rodadas utilizando a semente 2026.

São calculadas as frequências absolutas e relativas das combinações, a média do lucro líquido, o desvio padrão amostral e o RTP observado. Os resultados são comparados com as probabilidades teóricas e apresentados em tabela e gráfico.

### Experimento 2 — Comportamento da média acumulada

Compara três sequências de 10.000 rodadas, utilizando as sementes 10, 2026 e 123456.

A média acumulada é analisada após 100, 1.000 e 10.000 rodadas. O experimento permite observar a variação das médias e sua tendência de aproximação ao valor esperado teórico de −0,16 crédito por rodada.

Também verifica a reprodutibilidade dos resultados quando a mesma semente e o mesmo procedimento são utilizados.

### Experimento 3 — Simulação de participantes

Simula 100 participantes virtuais. Cada um começa com 100 créditos, aposta 1 crédito por rodada e pode jogar até 500 rodadas, encerrando a sessão caso não tenha saldo suficiente para outra aposta.

São analisados:

- Proporções de participantes com ganho, empate ou perda.
- Proporção de participantes que esgotaram o saldo.
- Média e mediana dos saldos finais.
- Trajetórias de saldo dos cinco primeiros participantes.

O experimento utiliza a semente 42 e mantém a sequência do gerador aleatório entre os participantes.

### Experimento 4 — Probabilidade condicional

Utiliza as 10.000 rodadas do primeiro experimento para analisar os 9.999 pares de rodadas consecutivas.

Compara a frequência de vitória na rodada seguinte em duas situações: quando a rodada anterior teve prêmio e quando não teve prêmio.

O objetivo é investigar a independência dos sorteios e discutir a falácia do jogador, segundo a qual resultados anteriores alterariam a probabilidade de vitória futura.

### Experimento 5 — Comparação das tabelas de pagamento

Compara a tabela original com outra que aumenta todos os prêmios em 10%.

As duas tabelas são aplicadas à mesma sequência de resultados do primeiro experimento, sem realizar novos sorteios.

São comparados a frequência observada de vitórias, o prêmio bruto médio, o lucro médio e os RTPs teórico e observado. Dessa forma, é possível analisar o efeito da mudança nos pagamentos mantendo os resultados aleatórios constantes.

## 📊 Indicadores estatísticos

O simulador utiliza os seguintes indicadores:

| Indicador | Finalidade |
|---|---|
| Frequência absoluta | Quantidade de ocorrências de cada resultado |
| Frequência relativa | Proporção de ocorrências em relação ao total |
| Média | Representa o resultado médio observado |
| Mediana | Representa o valor central dos dados ordenados |
| Desvio padrão amostral | Mede a dispersão dos lucros em torno da média |
| Valor esperado | Representa a média teórica do modelo |
| RTP | Mede o retorno bruto em relação ao total apostado |
| Probabilidade condicional | Estima a ocorrência de um evento considerando outro evento anterior |

## 🛠️ Tecnologias utilizadas

- **Python:** implementação do simulador e dos cálculos estatísticos.
- **Random:** geração de números pseudoaleatórios.
- **Statistics:** cálculo de medidas estatísticas.
- **CSV:** exportação dos resultados.
- **Matplotlib:** geração de gráficos.
- **VS Code:** ambiente de desenvolvimento.

## 🚀 Como executar o projeto

### Pré-requisitos

- Python 3.10 ou superior.
- Visual Studio Code ou outro ambiente compatível com Python.
- Biblioteca Matplotlib para a geração dos gráficos.

### 1. Clone o repositório

```bash
git clone https://github.com/alicelour/Trabalho_prob_est.git
```

### 2. Acesse a pasta do projeto

```bash
cd Trabalho_prob_est
```

### 3. Instale a dependência de gráficos

```bash
python -m pip install matplotlib
```

### 4. Execute o simulador

```bash
python main.py
```

### 5. Escolha uma opção no menu

- **Opção 1:** executa todos os experimentos.
- **Opção 2:** permite executar um experimento específico.
- **Opção 0:** encerra o programa.

Após a execução, os arquivos gerados ficam organizados na pasta `resultados/`.

## 📁 Arquivos gerados

| Arquivo | Descrição |
|---|---|
| `e1_distribuicao.csv` | Frequências e estatísticas do primeiro experimento |
| `e1_rodadas.csv` | Histórico das rodadas simuladas |
| `e2_medias.csv` | Médias acumuladas das diferentes sementes |
| `e3_participantes.csv` | Resultados dos participantes virtuais |
| `e4_condicional.csv` | Contagens e probabilidades condicionais |
| `e5_comparacao.csv` | Comparação entre as tabelas de pagamento |
| `ambiente.csv` | Informações do ambiente de execução |

O programa também gera gráficos em PNG para visualizar a distribuição dos resultados, as médias acumuladas e as trajetórias de saldo.

## 🔁 Reprodutibilidade dos experimentos

O simulador utiliza sementes fixas para inicializar o gerador pseudoaleatório. Isso permite reproduzir as sequências de resultados quando são mantidos o mesmo procedimento, as mesmas sementes e um ambiente compatível.

A repetição dos resultados não significa que os valores observados sejam iguais aos teóricos. Significa apenas que a mesma amostra simulada foi reproduzida.

Para analisar outras sequências, podem ser utilizadas sementes diferentes, como ocorre no segundo experimento.

## 💡 Conclusão

O projeto demonstra como conceitos de probabilidade e estatística podem ser aplicados à análise de um sistema aleatório. A comparação entre valores teóricos e observados evidencia a influência da variação amostral, enquanto os experimentos de médias acumuladas e probabilidades condicionais permitem discutir convergência estatística, independência e interpretações equivocadas sobre sequências de resultados.

Além disso, a comparação das tabelas de pagamento mostra como alterações nos prêmios modificam o retorno esperado sem necessariamente alterar a probabilidade de vitória.

O simulador reforça a importância de utilizar modelos matemáticos, experimentação computacional e análise crítica para interpretar resultados de maneira fundamentada.
