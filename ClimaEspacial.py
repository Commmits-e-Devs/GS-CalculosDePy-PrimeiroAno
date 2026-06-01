import random
import time

LIMITE_RADIACAO_SEGURO_MEV = 85.0

lista_de_satelites_proprios = [
    {"identificador": "FLY-GEO-1", "altitude_atual": 600, "status": "Operacional"},
    {"identificador": "FLY-GEO-2", "altitude_atual": 610, "status": "Operacional"},
    {"identificador": "FLY-GEO-3", "altitude_atual": 1200, "status": "Operacional"},
]

def obter_leitura_sensores_solares():
    if random.randint(1, 10) <= 3:
        return round(random.uniform(86.0, 120.0), 2)
    return round(random.uniform(15.0, 65.0), 2)

def gerenciar_clima_espacial_frota(lista_de_satelites):
    print("\n" + "=" * 60)
    print("\tFLYSPACE - MONITORAMENTO GEOMAGNÉTICO DE RADIAÇÃO")
    print("=" * 60)
    time.sleep(0.8)

    nivel_radiacao_atual = obter_leitura_sensores_solares()
    print(f"[TELEMETRIA]: Fluxo de Prótons Energéticos detectado: {nivel_radiacao_atual} MeV")
    print(f"[ANÁLISE DE SEGURANÇA]: Limiar Crítico de Domínio = {LIMITE_RADIACAO_SEGURO_MEV} MeV")

    if nivel_radiacao_atual > LIMITE_RADIACAO_SEGURO_MEV:
        print(f"\nALERTA MODELO MATEMÁTICO: {nivel_radiacao_atual} MeV > {LIMITE_RADIACAO_SEGURO_MEV} MeV!")
        print("Tempestade Solar Ativa. Executando interrupção de barramento elétrico...\n")
        time.sleep(1.0)

        for satelite in lista_de_satelites:
            print(f"Modificando {satelite['identificador']}:")
            print("-> Isolando painéis solares e suspendendo transmissão de rádio...")
            satelite["status"] = "Safe Mode (Modo de Segurança)"
            print(f"-> [STATUS ATUALIZADO]: {satelite['status']}")
            time.sleep(0.4)
        print("\nToda a frota ativa encontra-se protegida contra surtos de radiação.")
    else:
        print(f"\n[CONDIÇÃO ESTÁVEL]: {nivel_radiacao_atual} MeV <= {LIMITE_RADIACAO_SEGURO_MEV} MeV.")
        print("Magnetosfera controlada. Mantendo frotas em regime de alta performance.\n")
        for satelite in lista_de_satelites:
            satelite["status"] = "Operacional"

    print("=" * 60)
    print("\t\tVARREDURA DE CLIMA FINALIZADA")
    print("=" * 60 + "\n")