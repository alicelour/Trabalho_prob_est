"""
Maquina Estatistica - Probabilidade, apostas e pensamento critico
Simulador academico - somente creditos ficticios.

Requisitos:
- Python 3.10+
- Biblioteca padrao (csv, random, statistics, pathlib)
- Gera CSVs e graficos PNG (matplotlib e necessario para os graficos).
"""

import csv
import random
import sys
from pathlib import Path
from statistics import mean, median, stdev
from itertools import product

# ------------------------- MODELO DA MAQUINA -------------------------

SIMBOLOS = ("A", "B", "C", "D", "E")
SEQUENCIA_ROLO = SIMBOLOS
APOSTA = 1.0
TOTAL_RODADAS = 10_000
DIRETORIO_RESULTADOS = Path("resultados")

PAGAMENTOS = {
    ("A", "A", "A"): 5.0,
    ("B", "B", "B"): 10.0,
    ("C", "C", "C"): 15.0,
    ("D", "D", "D"): 25.0,
    ("E", "E", "E"): 50.0,
}
TRIPLAS_PREMIADAS = tuple(PAGAMENTOS.keys())
ESPACO_AMOSTRAL = list(product(SIMBOLOS, repeat=3))


def sortear_coluna(rng):
    """Sorteia uma parada K e monta a coluna circular topo-centro-base."""
    k = rng.randrange(len(SEQUENCIA_ROLO))
    n = len(SEQUENCIA_ROLO)
    return (
        SEQUENCIA_ROLO[k],
        SEQUENCIA_ROLO[(k + 1) % n],
        SEQUENCIA_ROLO[(k + 2) % n],
    )


def executar_rodada(rng):
    """Sorteia os tres rolos e avalia somente a linha central."""
    colunas = [sortear_coluna(rng) for _ in range(3)]
    resultado = tuple(coluna[1] for coluna in colunas)
    pagamento = PAGAMENTOS.get(resultado, 0.0)
    lucro = pagamento - APOSTA
    return {
        "rolo_1": "/".join(colunas[0]),
        "rolo_2": "/".join(colunas[1]),
        "rolo_3": "/".join(colunas[2]),
        "resultado_central": "-".join(resultado),
        "premiado": pagamento > 0,
        "premio_bruto": pagamento,
        "lucro": lucro,
    }


def simular_rodadas(quantidade, semente):
    """Executa uma sequencia reproduzivel e retorna todos os resultados."""
    rng = random.Random(semente)
    historico = []
    for numero in range(1, quantidade + 1):
        rodada = executar_rodada(rng)
        rodada["rodada"] = numero
        rodada["semente"] = semente
        rodada["aposta"] = APOSTA
        historico.append(rodada)
    return historico


def calcular_teoria():
    total = len(ESPACO_AMOSTRAL)
    distribuicao = []
    for resultado in TRIPLAS_PREMIADAS:
        distribuicao.append({
            "resultado": "-".join(resultado),
            "lucro": PAGAMENTOS[resultado] - APOSTA,
            "probabilidade": 1 / total,
        })
    distribuicao.append({
        "resultado": "Outras combinacoes",
        "lucro": -APOSTA,
        "probabilidade": (total - len(TRIPLAS_PREMIADAS)) / total,
    })
    premio_esperado = sum(PAGAMENTOS.values()) / total
    lucro_esperado = premio_esperado - APOSTA
    rtp = premio_esperado / APOSTA * 100
    return total, distribuicao, premio_esperado, lucro_esperado, rtp


def estatisticas(historico):
    lucros = [item["lucro"] for item in historico]
    pagamentos = [item["premio_bruto"] for item in historico]
    apostas = [item["aposta"] for item in historico]
    n = len(historico)
    total_apostado = sum(apostas)
    return {
        "n": n,
        "premios": sum(item["premiado"] for item in historico),
        "frequencia_premio": sum(item["premiado"] for item in historico) / n,
        "lucro_medio": mean(lucros),
        "mediana_lucro": median(lucros),
        "desvio_amostral": stdev(lucros) if n > 1 else 0.0,
        "lucro_total": sum(lucros),
        "pagamento_total": sum(pagamentos),
        "total_apostado": total_apostado,
        "rtp_observado": sum(pagamentos) / total_apostado * 100 if total_apostado else 0.0,
    }


def salvar_csv(nome, linhas):
    DIRETORIO_RESULTADOS.mkdir(exist_ok=True)
    caminho = DIRETORIO_RESULTADOS / nome
    if not linhas:
        return caminho
    with caminho.open("w", newline="", encoding="utf-8-sig") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=list(linhas[0].keys()), delimiter=";")
        escritor.writeheader()
        escritor.writerows(linhas)
    return caminho


def gerar_graficos():
    """Gera graficos requeridos. Se matplotlib nao estiver instalado, informa como instalar."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("\nMatplotlib nao encontrado. Instale com: python -m pip install matplotlib")
        return

    DIRETORIO_RESULTADOS.mkdir(exist_ok=True)

    # E1: teoria x frequencia observada para os seis resultados.
    if "e1" in RESULTADOS:
        hist = RESULTADOS["e1"]
        contagens = {}
        categorias = [f"{a}-{b}-{c}" for a, b, c in TRIPLAS_PREMIADAS] + ["Outras combinacoes"]
        for cat in categorias:
            contagens[cat] = 0
        for item in hist:
            chave = item["resultado_central"] if item["premiado"] else "Outras combinacoes"
            contagens[chave] += 1
        probs_teoricas = [1 / 125] * 5 + [120 / 125]
        frequencias = [contagens[cat] / len(hist) for cat in categorias]
        x = list(range(len(categorias)))
        largura = 0.38
        plt.figure(figsize=(10, 5))
        plt.bar([i - largura/2 for i in x], probs_teoricas, largura, label="Probabilidade teorica")
        plt.bar([i + largura/2 for i in x], frequencias, largura, label="Frequencia observada")
        plt.xticks(x, categorias, rotation=20)
        plt.ylabel("Proporcao")
        plt.title("E1 - Probabilidade teorica x frequencia observada")
        plt.legend()
        plt.tight_layout()
        plt.savefig(DIRETORIO_RESULTADOS / "e1_frequencias.png", dpi=150)
        plt.close()

    if (
    "e2" in RESULTADOS
    and all(
        semente in RESULTADOS["e2"]
        for semente in (10, 2026, 123456)
    )
):
        # E2: medias acumuladas em 3 sementes.
        plt.figure(figsize=(10, 5))
        for semente in (10, 2026, 123456):
            hist_e2 = RESULTADOS["e2"][semente]
            acumulado, valores = 0.0, []
            for i, item in enumerate(hist_e2, start=1):
                acumulado += item["lucro"]
                if i % 10 == 0 or i == 1:
                    valores.append((i, acumulado / i))
            plt.plot([p[0] for p in valores], [p[1] for p in valores], label=f"Semente {semente}")
        plt.axhline(-0.16, linestyle="--", label="Esperanca teorica (-0,16)")
        plt.xlabel("Numero de rodadas")
        plt.ylabel("Lucro medio acumulado (creditos)")
        plt.title("E2 - Lei dos Grandes Numeros")
        plt.legend()
        plt.tight_layout()
        plt.savefig(DIRETORIO_RESULTADOS / "e2_medias_acumuladas.png", dpi=150)
        plt.close()

    if "e3" in RESULTADOS:
        # E3: trajetorias dos cinco primeiros participantes, saldo constante apos parada.
        plt.figure(figsize=(10, 5))
        for participante, dados in enumerate(RESULTADOS["e3"][:5], start=1):
            saldo = 100.0
            trajetoria = [saldo]
            for lucro in dados["lucros"]:
                saldo += lucro
                trajetoria.append(saldo)
            while len(trajetoria) < 501:
                trajetoria.append(trajetoria[-1])
            plt.plot(range(len(trajetoria)), trajetoria, label=f"Participante {participante}")
        plt.xlabel("Rodada")
        plt.ylabel("Saldo (creditos)")
        plt.title("E3 - Trajetoria dos cinco primeiros participantes")
        plt.legend()
        plt.tight_layout()
        plt.savefig(DIRETORIO_RESULTADOS / "e3_saldos.png", dpi=150)
        plt.close()

    plt.close("all")


def experimento_1():
    print("\n========== EXPERIMENTO 1: FREQUENCIAS ==========")
    hist = simular_rodadas(TOTAL_RODADAS, 2026)
    RESULTADOS["e1"] = hist
    stats = estatisticas(hist)
    total, distribuicao, _, _, _ = calcular_teoria()
    linhas = []
    for item in distribuicao:
        resultado = item["resultado"]
        if resultado == "Outras combinacoes":
            contagem = sum(not r["premiado"] for r in hist)
        else:
            contagem = sum(r["resultado_central"] == resultado for r in hist)
        linhas.append({
            "resultado": resultado,
            "lucro_creditos": item["lucro"],
            "probabilidade_teorica": item["probabilidade"],
            "contagem": contagem,
            "frequencia_relativa": contagem / len(hist),
        })
    salvar_csv("e1_distribuicao.csv", linhas)
    salvar_csv("e1_rodadas.csv", hist)
    print(f"Rodadas: {stats['n']}")
    print(f"Premios: {stats['premios']} ({stats['frequencia_premio']*100:.2f}%)")
    print(f"Lucro medio: {stats['lucro_medio']:.4f} creditos (referencia: -0.16)")
    print(f"Desvio-padrao amostral: {stats['desvio_amostral']:.4f} creditos")
    print(f"RTP observado: {stats['rtp_observado']:.2f}% (teorico: 84.00%)")
    print(f"Arquivos: resultados/e1_distribuicao.csv e resultados/e1_rodadas.csv")


def experimento_2():
    print("\n========== EXPERIMENTO 2: MONTE CARLO E LGN ==========")
    sementes = (10, 2026, 123456)
    RESULTADOS["e2"] = {}
    linhas = []
    for semente in sementes:
        hist = RESULTADOS["e1"] if semente == 2026 else simular_rodadas(TOTAL_RODADAS, semente)
        RESULTADOS["e2"][semente] = hist
        acumulado = 0.0
        medias = {}
        for i, item in enumerate(hist, start=1):
            acumulado += item["lucro"]
            if i in (100, 1000, 10000):
                medias[i] = acumulado / i
        linhas.append({
            "semente": semente,
            "media_100": medias[100],
            "media_1000": medias[1000],
            "media_10000": medias[10000],
        })
    salvar_csv("e2_medias.csv", linhas)
    print("Medias acumuladas:")
    for linha in linhas:
        print(f"Semente {linha['semente']}: 100={linha['media_100']:.4f}; "
              f"1.000={linha['media_1000']:.4f}; 10.000={linha['media_10000']:.4f}")
    repeticao = simular_rodadas(10, 2026)
    primeiros = [(x["resultado_central"], x["lucro"]) for x in repeticao]
    primeiros_e1 = [(x["resultado_central"], x["lucro"]) for x in RESULTADOS["e1"][:10]]
    print(f"Reproducao dos dez primeiros resultados: {'SIM' if primeiros == primeiros_e1 else 'NAO'}")
    print("Arquivo: resultados/e2_medias.csv")


def experimento_3():
    print("\n========== EXPERIMENTO 3: SALDO LIMITADO ==========")
    rng = random.Random(42)  # inicializado uma vez para toda a sequencia de participantes
    participantes = []
    for numero in range(1, 101):
        saldo = 100.0
        lucros = []
        rodada = 0
        while rodada < 500 and saldo >= APOSTA:
            resultado = executar_rodada(rng)
            saldo += resultado["lucro"]
            lucros.append(resultado["lucro"])
            rodada += 1
        participantes.append({
            "participante": numero,
            "saldo_inicial": 100.0,
            "saldo_final": saldo,
            "rodadas": rodada,
            "esgotou": saldo < APOSTA,
            "resultado": "ganho" if saldo > 100 else "empate" if saldo == 100 else "perda",
            "lucros": lucros,
        })
    RESULTADOS["e3"] = participantes
    linhas = [{k: v for k, v in p.items() if k != "lucros"} for p in participantes]
    salvar_csv("e3_participantes.csv", linhas)
    ganhos = sum(p["resultado"] == "ganho" for p in participantes)
    empates = sum(p["resultado"] == "empate" for p in participantes)
    perdas = sum(p["resultado"] == "perda" for p in participantes)
    esgotados = sum(p["esgotou"] for p in participantes)
    saldos = [p["saldo_final"] for p in participantes]
    print(f"Ganho: {ganhos}% | Empate: {empates}% | Perda: {perdas}%")
    print(f"Esgotamento: {esgotados}% (subconjunto das perdas)")
    print(f"Saldo final medio: {mean(saldos):.2f}; mediano: {median(saldos):.2f} creditos")
    print("Arquivo: resultados/e3_participantes.csv")


def experimento_4():
    print("\n========== EXPERIMENTO 4: PROBABILIDADE CONDICIONAL ==========")
    hist = RESULTADOS.get("e1")
    if not hist:
        hist = simular_rodadas(TOTAL_RODADAS, 2026)
        RESULTADOS["e1"] = hist
    grupos = {
        "Apos premio": {"pares": 0, "premios_seguinte": 0},
        "Apos sem premio": {"pares": 0, "premios_seguinte": 0},
    }
    for anterior, atual in zip(hist, hist[1:]):
        chave = "Apos premio" if anterior["premiado"] else "Apos sem premio"
        grupos[chave]["pares"] += 1
        if atual["premiado"]:
            grupos[chave]["premios_seguinte"] += 1
    linhas = []
    for grupo, dados in grupos.items():
        proporcao = dados["premios_seguinte"] / dados["pares"] if dados["pares"] else None
        linhas.append({
            "resultado_anterior": grupo,
            "total_pares": dados["pares"],
            "premios_na_rodada_seguinte": dados["premios_seguinte"],
            "proporcao_observada": proporcao,
        })
        print(f"{grupo}: {dados['premios_seguinte']}/{dados['pares']} "
              f"= {proporcao*100:.2f}%" if proporcao is not None else f"{grupo}: nao estimavel")
    salvar_csv("e4_condicional.csv", linhas)
    print("Referencia teorica em ambos os grupos: 4.00%")
    print("Arquivo: resultados/e4_condicional.csv")


def experimento_5():
    print("\n========== EXPERIMENTO 5: COMPARACAO DE PAGAMENTOS ==========")
    hist = RESULTADOS.get("e1")
    if not hist:
        hist = simular_rodadas(TOTAL_RODADAS, 2026)
        RESULTADOS["e1"] = hist
    linhas = []
    tabelas = {
        "Base": PAGAMENTOS,
        "Premios +10%": {k: v * 1.10 for k, v in PAGAMENTOS.items()},
    }
    for nome, tabela in tabelas.items():
        pagamentos = [
            tabela.get(tuple(item["resultado_central"].split("-")), 0.0)
            for item in hist
        ]
        lucros = [p - APOSTA for p in pagamentos]
        total_apostado = len(hist) * APOSTA
        premio_esperado = sum(tabela.values()) / 125
        linhas.append({
            "tabela": nome,
            "probabilidade_teorica_premio": 5 / 125,
            "frequencia_observada_premio": sum(p > 0 for p in pagamentos) / len(hist),
            "premio_medio_observado": mean(pagamentos),
            "lucro_medio_observado": mean(lucros),
            "rtp_teorico": premio_esperado / APOSTA * 100,
            "rtp_observado": sum(pagamentos) / total_apostado * 100,
        })
    salvar_csv("e5_comparacao.csv", linhas)
    for linha in linhas:
        print(f"{linha['tabela']}: chance premio={linha['probabilidade_teorica_premio']*100:.2f}%; "
              f"frequencia observada={linha['frequencia_observada_premio']*100:.2f}%; "
              f"lucro medio={linha['lucro_medio_observado']:.4f}; "
              f"RTP teorico={linha['rtp_teorico']:.2f}%; "
              f"RTP observado={linha['rtp_observado']:.2f}%")
    print("Arquivo: resultados/e5_comparacao.csv")


def exibir_rodada():
    rng = random.Random()
    rodada = executar_rodada(rng)
    print("\n========== RODADA DEMONSTRATIVA ==========")
    print("Rolos (topo/centro/base):")
    print(f"Rolo 1: {rodada['rolo_1']}")
    print(f"Rolo 2: {rodada['rolo_2']}")
    print(f"Rolo 3: {rodada['rolo_3']}")
    print(f"Linha central: {rodada['resultado_central']}")
    print(f"Premio bruto: {rodada['premio_bruto']:.2f} creditos")
    print(f"Lucro liquido: {rodada['lucro']:.2f} creditos")


def salvar_informacoes_ambiente():
    import platform
    try:
        import matplotlib
        matplotlib_versao = matplotlib.__version__
    except ImportError:
        matplotlib_versao = "nao instalado"
    linhas = [{
        "python": sys.version.split()[0],
        "plataforma": platform.platform(),
        "gerador": "random.Random / Mersenne Twister",
        "biblioteca_graficos": "matplotlib",
        "versao_matplotlib": matplotlib_versao,
        "aposta_creditos": APOSTA,
        "rodadas_experimentos": TOTAL_RODADAS,
    }]
    salvar_csv("ambiente.csv", linhas)


RESULTADOS = {}


def main():
    print("=" * 62)
    print("MAQUINA ESTATISTICA - Probabilidade, apostas e pensamento critico")
    print("Simulador academico - somente creditos ficticios")
    print("=" * 62)
    total, distribuicao, premio_esperado, lucro_esperado, rtp = calcular_teoria()
    print(f"Combinacoes centrais possiveis: {total}")
    print("Probabilidade de premio: 4.00% | Sem premio: 96.00%")
    print(f"Premio esperado: {premio_esperado:.2f} creditos | "
          f"Lucro esperado: {lucro_esperado:.2f} creditos | RTP teorico: {rtp:.2f}%")
    exibir_rodada()

    while True:
        print("\nEscolha uma opcao:")
        print("1 - Executar os cinco experimentos")
        print("2 - Executar apenas um experimento")
        print("0 - Sair")
        escolha = input("Opcao: ").strip()
        if escolha == "0":
            break
        elif escolha == "1":
            for funcao in (experimento_1, experimento_2, experimento_3, experimento_4, experimento_5):
                funcao()
            gerar_graficos()
            salvar_informacoes_ambiente()
            print("\nExperimentos concluidos. Resultados salvos na pasta 'resultados'.")
        elif escolha == "2":
            print("1-E1 | 2-E2 | 3-E3 | 4-E4 | 5-E5")
            qual = input("Experimento: ").strip()
            mapa = {"1": experimento_1, "2": experimento_2, "3": experimento_3,
                    "4": experimento_4, "5": experimento_5}
            if qual in mapa:
                mapa[qual]()
                if qual == "1":
                    RESULTADOS["e2"] = {2026: RESULTADOS["e1"]}
                gerar_graficos()
                salvar_informacoes_ambiente()
            else:
                print("Opcao invalida.")
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()
