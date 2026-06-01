import random
import time

LIMITE_RADIACAO_SEGURO_MEV = 85.0

lista_de_satelites_proprios = [
    {"identificador": "MEU-SAT-1", "altitude_atual": 600, "status": "Operacional"},
    {"identificador": "MEU-SAT-2", "altitude_atual": 610, "status": "Operacional"},
    {"identificador": "MEU-SAT-3", "altitude_atual": 1200, "status": "Operacional"},
]

def obter_leitura_sensores_solares():
    if random.randint(1, 10) <= 3:
        return round(random.uniform(86.0, 120.0), 2)
    return round(random.uniform(15.0, 65.0), 2)

def gerenciar_clima_espacial_frota(lista_de_satelites):
    print("\n" + "=" * 60)
    print("\tFLYSPACE - SISTEMA DE MONITORAMENTO DE CLIMA ESPACIAL")
    print("=" * 60)
    time.sleep(1.0)

    nivel_radiacao_atual = obter_leitura_sensores_solares()
    print(f"TELEMETRIA SOLAR ATUAL: {nivel_radiacao_atual} MeV")

    if nivel_radiacao_atual > LIMITE_RADIACAO_SEGURO_MEV:
        print(f"ALERTA CRÍTICO: Tempestade solar detectada! Nível acima de {LIMITE_RADIACAO_SEGURO_MEV} MeV.")
        print("Iniciando protocolo automático de salvaguarda eletrônica...\n")
        time.sleep(1.5)

        for satelite in lista_de_satelites:
            print(f"Modificando {satelite['identificador']}:")
            print("  -> Desligando cargas úteis e instrumentos não essenciais...")
            time.sleep(0.5)
            satelite["status"] = "Safe Mode (Modo de Segurança)"
            print(f"  -> Status atualizado: {satelite['status']}\n")
            time.sleep(0.5)

        print("Toda a frota Flyspace está protegida em Modo de Segurança.")
    else:
        print("Clima espacial estável. Ventos solares dentro da normalidade.")
        print("Mantendo todos os satélites em regime de operação total.\n")

        for satelite in lista_de_satelites:
            satelite["status"] = "Operacional"

    print("=" * 60)
    print("\t\tMONITORAMENTO DE CLIMA CONCLUÍDO")
    print("=" * 60 + "\n")