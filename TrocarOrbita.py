import random
import time
import math

RAIO_TERRA_KM = 6371.0
GM_TERRA = 398600.4418
DISTANCIA_LIMITE_SEGURANCA_KM = 15.0

lista_de_satelites_proprios = [
    {"identificador": "MEU-SAT-1", "altitude_atual": 600},
    {"identificador": "MEU-SAT-2", "altitude_atual": 610},
    {"identificador": "MEU-SAT-3", "altitude_atual": 620},
]


def calcular_velocidade_orbital(altitude_km):
    raio_orbital = RAIO_TERRA_KM + altitude_km
    velocidade = math.sqrt(GM_TERRA / raio_orbital)
    return round(velocidade, 3)


def calcular_periodo_orbital(altitude_km):
    raio_orbital = RAIO_TERRA_KM + altitude_km
    periodo_segundos = 2 * math.pi * math.sqrt((raio_orbital ** 3) / GM_TERRA)
    return round(periodo_segundos / 60, 2)


def calcular_delta_v(altitude_1, altitude_2):
    v1 = calcular_velocidade_orbital(altitude_1)
    v2 = calcular_velocidade_orbital(altitude_2)
    delta_v = abs(v2 - v1)
    return round(delta_v, 3)


def buscar_satelite_proximo():
    if random.randint(1, 10) <= 7:
        return {
            "id_concorrente": f"SAT-CONCORRENTE-{random.randint(100, 999)}",
            "distancia_km": round(random.uniform(2.0, 50.0), 1),
            "tempo_de_espera_segundos": random.randint(2, 5),
            "altitude_concorrente": round(random.uniform(580, 650), 1),
        }
    return None


def validar_se_nova_altitude_esta_vazia(altitude_para_testar):
    return random.randint(1, 100) <= 80


def realizar_manobra_com_desvio_incrementado(
        id_satelite, altitude_original, tempo_espera, altitude_concorrente
):
    velocidade_original = calcular_velocidade_orbital(altitude_original)
    periodo_original = calcular_periodo_orbital(altitude_original)

    print(f"\n--- ANÁLISE INICIAL DO SATÉLITE CONCORRENTE ---")
    print(f"Altitude: {altitude_concorrente} km")
    print(f"Velocidade: {calcular_velocidade_orbital(altitude_concorrente)} km/s")
    print()
    time.sleep(1.0)
    incrementos = [20, 40, 60]

    for numero_tentativa, incremento in enumerate(incrementos, 1):
        nova_altitude = altitude_original + incremento
        nova_velocidade = calcular_velocidade_orbital(nova_altitude)
        delta_v = calcular_delta_v(altitude_original, nova_altitude)
        novo_periodo = calcular_periodo_orbital(nova_altitude)

        print(f"TENTATIVA {numero_tentativa}:")
        print(f"Altitude proposta: {altitude_original} + {incremento} = {nova_altitude} km")
        print(f"Velocidade nessa órbita: {nova_velocidade} km/s")
        print(f"Período orbital: {novo_periodo} min")
        print(f"Combustível necessário (delta-v): {delta_v} km/s")
        print(f"Verificando disponibilidade da órbita...", end=" ")
        time.sleep(1.0)

        if validar_se_nova_altitude_esta_vazia(nova_altitude):
            print("LIBERADA")
            print(f"\nSUCESSO: Órbita {nova_altitude} km está disponível!")
            print(f"Executando desvio para {id_satelite}...")
            time.sleep(1.0)

            print(f"Elevando de {altitude_original} para {nova_altitude} km...")
            time.sleep(1.0)

            print(f"Aguardando tráfego do concorrente ({tempo_espera}s)...")
            time.sleep(tempo_espera)

            print(f"Retornando à órbita nominal de {altitude_original} km...")
            time.sleep(1.0)

            print(f"{id_satelite} estabilizado na posição original.")
            print(f"Velocidade nominal: {velocidade_original} km/s")
            print(f"Período: {periodo_original} min\n")
            time.sleep(1.0)
            return True
        else:
            print("OCUPADA")
            print(f"Órbita {nova_altitude} km indisponível. Tentando próxima altitude...\n")
            time.sleep(1.0)

    print("\n*** TODAS AS TENTATIVAS DE DESVIO SIMPLES FALHARAM ***")
    print("Executando manobra de aceleração para órbita superior...")
    print()
    time.sleep(1.0)

    return realizar_manobra_de_aceleracao(
        id_satelite, altitude_original, velocidade_original, periodo_original
    )


def realizar_manobra_de_aceleracao(id_satelite, altitude_original, vel_original, periodo_original):
    altitude_transferencia = altitude_original + 70
    vel_transferencia = calcular_velocidade_orbital(altitude_transferencia)
    periodo_transferencia = calcular_periodo_orbital(altitude_transferencia)

    delta_v_subida = calcular_delta_v(altitude_original, altitude_transferencia)
    delta_v_retorno = calcular_delta_v(altitude_transferencia, altitude_original)

    print("--- MANOBRA DE ACELERAÇÃO E TRANSFERÊNCIA ---\n")
    time.sleep(0.5)

    print(f"FASE 1: ACELERAÇÃO TANGENCIAL")
    print(f"Altitude atual: {altitude_original} km")
    print(f"Velocidade atual: {vel_original} km/s")
    print(f"Acelerando satélite...")
    time.sleep(0.5)

    print(f"Delta-v aplicado: {delta_v_subida} km/s")
    print(f"Iniciando ascensão para órbita de transferência\n")
    time.sleep(1.5)

    print(f"FASE 2: ÓRBITA DE TRANSFERÊNCIA")
    print(f"Altitude alcançada: {altitude_transferencia} km")
    print(f"Velocidade na transferência: {vel_transferencia} km/s")
    print(f"Período: {periodo_transferencia} min")
    print(f"Aguardando para circularizar órbita...\n")
    time.sleep(1.5)

    print(f"FASE 3: CIRCULARIZAÇÃO")
    print(f"Aplicando correção de velocidade")
    print(f"Órbita {altitude_transferencia} km agora está estável e segura")
    print(f"Esperando afastamento do tráfego...\n")
    time.sleep(2.0)

    print(f"FASE 4: RETORNO À ÓRBITA NOMINAL")
    print(f"Delta-v de retorno: {delta_v_retorno} km/s")
    print(f"Descendendo de {altitude_transferencia} para {altitude_original} km...")
    time.sleep(1.0)

    print(f"  Finalizando manobra de retorno...")
    time.sleep(1.0)

    print(f"\nSUCESSO: {id_satelite} retornou à órbita nominal")
    print(f"Altitude: {altitude_original} km")
    print(f"Velocidade: {vel_original} km/s")
    print(f"Período: {periodo_original} min")
    print(f"Combustível total gasto: {delta_v_subida + delta_v_retorno:.3f} km/s\n")
    time.sleep(1.0)

    return True


def executar_monitoramento_satelite(satelite_atual):
    print("\n" + "=" * 60)
    print(f"\t\tMONITORAMENTO: {satelite_atual['identificador']}")
    print(f"\t\tÓrbita atual: {satelite_atual['altitude_atual']} km")
    print("=" * 60)
    print()
    time.sleep(1.0)

    dados_concorrente = buscar_satelite_proximo()

    if dados_concorrente is not None:
        distancia = dados_concorrente["distancia_km"]
        id_concorrente = dados_concorrente["id_concorrente"]
        altitude_concorrente = dados_concorrente["altitude_concorrente"]

        print(f"TRÁFEGO DETECTADO: {id_concorrente}")
        print(f"Distância: {distancia} km")
        print(f"Altitude: {altitude_concorrente} km")
        print()
        time.sleep(1.0)

        if distancia <= DISTANCIA_LIMITE_SEGURANCA_KM:
            print(f"CRÍTICO: Distância {distancia} km <= Limite de segurança {DISTANCIA_LIMITE_SEGURANCA_KM} km")
            print("Iniciando protocolo de evasão...")
            time.sleep(1.0)

            realizar_manobra_com_desvio_incrementado(
                satelite_atual["identificador"],
                satelite_atual["altitude_atual"],
                dados_concorrente["tempo_de_espera_segundos"],
                altitude_concorrente,
            )
        else:
            print(f"SEGURO: Distância {distancia} km > Limite {DISTANCIA_LIMITE_SEGURANCA_KM} km")
            print("Mantendo rota. Monitorando aproximação...\n")
            time.sleep(1.0)
    else:
        print("SEGURO: Nenhuma detecção no radar\n")
        time.sleep(1.0)

    print("-" * 60)
    time.sleep(0.5)


def executar_sistema_geral_anticolisao(lista_de_satelites):
    print("\n" + "=" * 60)
    print("\tSISTEMA DE GERENCIAMENTO DE TRÁFEGO ESPACIAL")
    print("=" * 60)
    time.sleep(1.5)

    for satelite in lista_de_satelites:
        executar_monitoramento_satelite(satelite)

    print("\n" + "=" * 60)
    print("\t\tVARREDURA DE FROTA CONCLUÍDA")
    print("=" * 60 + "\n")