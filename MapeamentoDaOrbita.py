import urllib.request
import ssl
import math

RAIO_TERRA_KM = 6371.0
MI_TERRA = 3.986004418e14

def baixar_dados_tle():
    url = 'https://raw.githubusercontent.com/mrmykey/tlecdn/main/active.txt'
    print("Conectando com o servidor de dados espelho...")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    try:
        contexto_seguranca = ssl._create_unverified_context()
        requisicao = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(requisicao, context=contexto_seguranca) as resposta:
            print("Dados recebidos com sucesso! Processando as órbitas...")
            return resposta.read().decode('utf-8').splitlines()

    except Exception as erro:
        print("\n[ERRO DE CONEXÃO]")
        print(f"Não foi possível baixar os dados: {erro}")
        return []

def calcular_altitude(movimento_medio_dia):
    if movimento_medio_dia <= 0:
        return -1

    n_rad_s = (movimento_medio_dia * 2 * math.pi) / 86400.0

    semi_eixo_maior_m = (MI_TERRA / (n_rad_s ** 2)) ** (1.0 / 3.0)

    return (semi_eixo_maior_m / 1000.0) - RAIO_TERRA_KM

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
        "LEO (Baixa)": 0,
        "MEO (Média)": 0,
        "GEO (Geoestacionária)": 0,
        "HEO / Outras": 0,
        "Inválida/Erro": 0
    }

    for i in range(0, len(linhas_tle) - 2, 3):
        linha2 = linhas_tle[i + 2]

        if not linha2.startswith('2 '):
            continue

        try:
            movimento_medio = float(linha2[52:63].strip())
            altitude = calcular_altitude(movimento_medio)
            categoria = classificar_orbita(altitude)

            contagem[categoria] += 1

        except ValueError:
            contagem["Inválida/Erro"] += 1

    return contagem

def exibir_relatorio(resultados):
    print("\n" + "=" * 45)
    print(" QUANTIDADE DE SATÉLITES POR ÓRBITA")
    print("=" * 45)

    total_validos = 0
    for categoria, quantidade in resultados.items():
        if categoria != "Inválida/Erro":
            print(f" {categoria:<25} | {quantidade:>6} ")
            total_validos += quantidade

    print("-" * 45)
    print(f" {'TOTAL ATIVOS':<25} | {total_validos:>6} ")
    print("=" * 45)

def mapeamentoDaOrbita():
    linhas_texto = baixar_dados_tle()
    if linhas_texto:
        resultados = processar_satelites(linhas_texto)
        exibir_relatorio(resultados)