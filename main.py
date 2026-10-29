
import random
import csv
from itertools import product
from statistics import mean, median, pstdev

# ==================================================
# 1. CONFIGURACOES DO JOGO
# ==================================================

SIMBOLOS = ["A", "B", "C", "D", "E"]

# Substitua pelas cinco triplas premiadas do enunciado.
TRIPLAS_PREMIADAS = [
    ("A", "A", "A"),
    ("B", "B", "B"),
    ("C", "C", "C"),
    ("D", "D", "D"),
    ("E", "E", "E"),
]

# PAGAMENTOS PROVISORIOS: substitua pela tabela do professor.
# Cada valor representa o pagamento TOTAL, incluindo a aposta.
PAGAMENTOS = {
    ("A", "A", "A"): 2,
    ("B", "B", "B"): 3,
    ("C", "C", "C"): 5,
    ("D", "D", "D"): 10,
    ("E", "E", "E"): 20,
}

APOSTA_MINIMA = 1.00


# ==================================================
# 2. ESPACO AMOSTRAL E PROBABILIDADES TEORICAS
# ==================================================

ESPACO_AMOSTRAL = list(product(SIMBOLOS, repeat=3))

def calcular_probabilidades():
    total = len(ESPACO_AMOSTRAL)
    prob_premio = len(TRIPLAS_PREMIADAS) / total
    prob_sem_premio = 1 - prob_premio

    return total, prob_premio, prob_sem_premio


# ==================================================
# 3. SORTEIO DOS TRES ROLOS
# ==================================================

def sortear_resultado():
    rolo1 = random.choice(SIMBOLOS)
    rolo2 = random.choice(SIMBOLOS)
    rolo3 = random.choice(SIMBOLOS)

    return (rolo1, rolo2, rolo3)


def calcular_pagamento(resultado, aposta):
    multiplicador = PAGAMENTOS.get(resultado, 0)
    pagamento = aposta * multiplicador

    return pagamento, multiplicador


# ==================================================
# 4. SIMULACAO DE UMA RODADA
# ==================================================

def executar_rodada(aposta):
    resultado = sortear_resultado()
    pagamento, multiplicador = calcular_pagamento(
        resultado, aposta
    )

    lucro = pagamento - aposta
    premiado = resultado in TRIPLAS_PREMIADAS

    return {
        "resultado": resultado,
        "premiado": premiado,
        "aposta": aposta,
        "multiplicador": multiplicador,
        "pagamento": pagamento,
        "lucro": lucro,
    }


# ==================================================
# 5. ESPERANCA MATEMATICA E RTP
# ==================================================

def calcular_esperanca(aposta=1.0):
    total = len(ESPACO_AMOSTRAL)
    esperanca_lucro = 0.0
    pagamento_esperado = 0.0

    for resultado in ESPACO_AMOSTRAL:
        pagamento, _ = calcular_pagamento(
            resultado, aposta
        )

        probabilidade = 1 / total
        lucro = pagamento - aposta

        esperanca_lucro += probabilidade * lucro
        pagamento_esperado += probabilidade * pagamento

    rtp = (pagamento_esperado / aposta) * 100

    return esperanca_lucro, pagamento_esperado, rtp


# ==================================================
# 6. SIMULACAO DE VARIAS RODADAS
# ==================================================

def simular(quantidade, aposta):
    historico = []
    saldo = 0.0

    for rodada in range(1, quantidade + 1):
        dados = executar_rodada(aposta)

        saldo += dados["lucro"]

        historico.append({
            "rodada": rodada,
            "rolo_1": dados["resultado"][0],
            "rolo_2": dados["resultado"][1],
            "rolo_3": dados["resultado"][2],
            "premiado": dados["premiado"],
            "aposta": aposta,
            "multiplicador": dados["multiplicador"],
            "pagamento": dados["pagamento"],
            "lucro": dados["lucro"],
            "saldo_acumulado": saldo,
        })

    return historico


# ==================================================
# 7. ANALISE ESTATISTICA
# ==================================================


def analisar_resultados(historico):
    quantidade = len(historico)
    lucros = [item["lucro"] for item in historico]
    premiados = sum(item["premiado"] for item in historico)
    sem_premio = quantidade - premiados
    lucro_total = sum(lucros)

    print("\n========== RESULTADOS ==========")
    print(f"Rodadas realizadas: {quantidade}")
    print(f"Com premio: {premiados} ({premiados / quantidade * 100:.2f}%)")
    print(f"Sem premio: {sem_premio} ({sem_premio / quantidade * 100:.2f}%)")
    print(f"Lucro medio por rodada: R$ {mean(lucros):.2f}")
    print(f"Mediana do lucro: R$ {median(lucros):.2f}")
    print(f"Desvio-padrao: R$ {pstdev(lucros):.2f}")
    print(f"Resultado acumulado: R$ {lucro_total:.2f}")

    print("\n========== VALORES TEORICOS ==========")
    print("Probabilidade de premio: 4.00%")
    print("Probabilidade sem premio: 96.00%")

    if lucro_total < 0:
        print(f"Prejuizo total: R$ {abs(lucro_total):.2f}")
    elif lucro_total > 0:
        print(f"Lucro total: R$ {lucro_total:.2f}")
    else:
        print("Resultado final: R$ 0.00")

    return premiados / quantidade


# ==================================================
# 8. PROBABILIDADE CONDICIONAL
# ==================================================

def analisar_probabilidade_condicional(historico):
    premios_apos_perda = 0
    perdas_anteriores = 0

    premios_apos_premio = 0
    premios_anteriores = 0

    for i in range(1, len(historico)):
        anterior = historico[i - 1]["premiado"]
        atual = historico[i]["premiado"]

        if anterior:
            premios_anteriores += 1
            if atual:
                premios_apos_premio += 1
        else:
            perdas_anteriores += 1
            if atual:
                premios_apos_perda += 1

    print("\n====== PROBABILIDADE CONDICIONAL ======")

    if perdas_anteriores > 0:
        print(
            "Premio apos perda: "
            f"{premios_apos_perda / perdas_anteriores * 100:.2f}%"
        )
    else:
        print("Nao houve perdas anteriores suficientes.")

    if premios_anteriores > 0:
        print(
            "Premio apos premio: "
            f"{premios_apos_premio / premios_anteriores * 100:.2f}%"
        )
    else:
        print("Nao houve premios anteriores suficientes.")

    print("Referencia teorica: 4% em cada rodada.")


# ==================================================
# 9. EXPORTACAO DOS DADOS
# ==================================================

def salvar_csv(historico, nome_arquivo="historico_simulacao.csv"):
    if not historico:
        print("Nao ha dados para salvar.")
        return

    with open(
        nome_arquivo,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as arquivo:
        campos = list(historico[0].keys())
        escritor = csv.DictWriter(
            arquivo,
            fieldnames=campos,
            delimiter=";"
        )

        escritor.writeheader()
        escritor.writerows(historico)

    print(f"\nDados salvos em: {nome_arquivo}")


# ==================================================
# 10. PROGRAMA PRINCIPAL
# ==================================================

def main():
    print("=" * 50)
    print("       MAQUINA ESTATISTICA")
    print(" Probabilidade, apostas e pensamento critico")
    print("=" * 50)

    total, prob_premio, prob_sem_premio = (
        calcular_probabilidades()
    )
 

    while True:
        try:
            quantidade = int(
                input("\nQuantidade de rodadas: ")
            )
            if quantidade > 0:
                break
            print("Informe um numero maior que zero.")
        except ValueError:
            print("Digite um numero inteiro valido.")

    while True:
        try:
            aposta = float(
                input("Valor apostado por rodada (R$): ")
                .replace(",", ".")
            )

            if aposta >= APOSTA_MINIMA:
                break

            print("A aposta minima e R$ 1,00.")
        except ValueError:
            print("Digite um valor valido.")

    print("\nExecutando simulacao...")

    historico = simular(quantidade, aposta)

    analisar_resultados(historico)
    analisar_probabilidade_condicional(historico)

    esperanca, pagamento_esperado, rtp = calcular_esperanca(aposta)

    print("\n========== RETORNO DA MAQUINA ==========")
    print(f"Pagamento esperado por rodada: R$ {pagamento_esperado:.2f}")
    print(f"Lucro esperado por rodada: R$ {esperanca:.2f}")
    print(f"RTP teorico: {rtp:.2f}%")


    salvar_csv(historico)


if __name__ == "__main__":
    main()
