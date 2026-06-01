import urllib.request
import ssl
import math
import time

RAIO_TERRA_KM = 6371.0
MI_TERRA = 3.986004418e14


def baixar_dados_tle():
    url = 'https://raw.githubusercontent.com/mrmykey/tlecdn/main/active.txt'
    print("\nConectando com o servidor NORAD/TLE espelho...")

    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        contexto_seguranca = ssl._create_unverified_context()
        requisicao = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(requisicao, context=contexto_seguranca) as resposta:
            print("Dados TLE recebidos com sucesso! Processando matrizes de órbita...")
            return resposta.read().decode('utf-8').splitlines()
    except Exception as erro:
        print("\n[ERRO DE CONEXÃO TELEMÉTRICA]")
        print(f"Não foi possível baixar os dados orbitais: {erro}")
        return []


def calcular_altitude(movimento_medio_dia, mostrar_passo=False):
    if movimento_medio_dia <= 0:
        return -1

    n_rad_s = (movimento_medio_dia * 2 * math.pi) / 86400.0

    semi_eixo_maior_m = (MI_TERRA / (n_rad_s ** 2)) ** (1.0 / 3.0)
    altitude_calculada = (semi_eixo_maior_m / 1000.0) - RAIO_TERRA_KM

    if mostrar_passo:
        print("\n--- DEMONSTRAÇÃO DO FLUXO MATEMÁTICO (KEPLER) ---")
        print(f" 1. Movimento Médio Convertido (n): {n_rad_s:.7f} rad/s")
        print(f" 2. Semi-eixo Maior Isolado (a): {semi_eixo_maior_m / 1000.0:.2f} km")
        print(f" 3. Altitude Líquida Resolvida (h = a - R_T): {altitude_calculada:.2f} km")
        print("-" * 50)

    return altitude_calculada


def classificar_orbita(altitude_km):
    if altitude_km < 0:
        return "Inválida/Erro"
    elif altitude_km <= 2000:
        return "LEO (Baixa)"
    elif altitude_km <= 35500:
        return "MEO (Média)"
    elif altitude_km <= 36000:
        return "GEO (Geoestacionária)"
    else:
        return "HEO / Outras"


def processar_satelites(linhas_tle):
    contagem = {
        "LEO (Baixa)": 0, "MEO (Média)": 0, "GEO (Geoestacionária)": 0,
        "HEO / Outras": 0, "Inválida/Erro": 0
    }

    primeiro = True
    for i in range(0, len(linhas_tle) - 2, 3):
        linha2 = linhas_tle[i + 2]
        if not linha2.startswith('2 '):
            continue

        try:
            movimento_medio = float(linha2[52:63].strip())

            altitude = calcular_altitude(movimento_medio, mostrar_passo=primeiro)
            primeiro = False

            categoria = classificar_orbita(altitude)
            contagem[categoria] += 1
        except ValueError:
            contagem["Inválida/Erro"] += 1

    return contagem


def exibir_relatorio(resultados):
    print("\n" + "=" * 50)
    print("RELATÓRIO ESTATÍSTICO DE COMPORTAMENTO ORBITAL")
    print("=" * 50)
    total_validos = 0
    for categoria, quantidade in resultados.items():
        if categoria != "Inválida/Erro":
            print(f"{categoria:<25} | {quantidade:>6} satélites")
            total_validos += quantidade
    print("-" * 50)
    print(f"{'TOTAL DE ATIVOS MAPEADOS':<25} | {total_validos:>6} ativos")
    print("=" * 50 + "\n")


def mapeamentoDaOrbita():
    print(f"[PARÂMETROS FIXOS]: Gμ = {MI_TERRA} m³/s² | Raio Terrestre = {RAIO_TERRA_KM} km")
    linhas_texto = baixar_dados_tle()
    if linhas_texto:
        resultados = processar_satelites(linhas_texto)
        exibir_relatorio(resultados)