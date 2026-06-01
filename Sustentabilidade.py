import time

LIMITE_MINIMO_COMBUSTIVEL_PORCENTO = 5.0
LIMITE_ALTITUDE_LEO_KM = 2000.0

lista_de_satelites_proprios = [
    {"identificador": "FLY-SUSTAIN-1", "altitude_atual": 550, "combustivel": 65.0, "ciclo_vida": "Ativo"},
    {"identificador": "FLY-SUSTAIN-2", "altitude_atual": 720, "combustivel": 3.2, "ciclo_vida": "Ativo"},
    {"identificador": "FLY-SUSTAIN-3", "altitude_atual": 2200, "combustivel": 4.1, "ciclo_vida": "Ativo"},
]

def avaliar_sustentabilidade_satelite(satelite):
    print(f"\nAUDITORIA AMBIENTAL: {satelite['identificador']}")
    print(f" -> Altitude Operacional: {satelite['altitude_atual']} km | Combustível Restante: {satelite['combustivel']}%")
    time.sleep(0.5)

    if satelite["combustivel"] <= LIMITE_MINIMO_COMBUSTIVEL_PORCENTO:
        print(f"GATILHO ATIVADO: Combustível ({satelite['combustivel']}%) <= Limiar Técnico ({LIMITE_MINIMO_COMBUSTIVEL_PORCENTO}%)")
        print("Iniciando cálculos para mitigação de lixo espacial (Diretriz IADC)...")
        time.sleep(0.8)

        if satelite["altitude_atual"] <= LIMITE_ALTITUDE_LEO_KM:
            satelite["ciclo_vida"] = "Desorbitado (Queima Atmosférica)"
            print(f"[REGRA AMBIENTAL]: Altitude <= {LIMITE_ALTITUDE_LEO_KM} km (Domínio LEO)")
            print(f"PROTOCOLO REENTRADA: Ignição retrógrada aplicada. Desintegração forçada na atmosfera.")
        else:
            satelite["ciclo_vida"] = "Desorbitado (Órbita Cemitério)"
            print(f"[REGRA AMBIENTAL]: Altitude > {LIMITE_ALTITUDE_LEO_KM} km (Domínio MEO/GEO)")
            print(f"PROTOCOLO CEMITÉRIO: Propulsão progressiva ativada para Órbita de Descarte Estável.")

        print(f"-> [NOVO STATUS DE CICLO]: {satelite['ciclo_vida']}")
    else:
        print("STATUS ADEQUADO: Autonomia estável para manutenção das operações programadas.")

    print("-" * 60)

def executar_auditoria_ambiental_espacial(lista_de_satelites):
    print("\n" + "=" * 60)
    print("\tFLYSPACE - CONTROLADOR DE SUSTENTABILIDADE ORBITAL")
    print("=" * 60)
    time.sleep(0.8)

    for satelite in lista_de_satelites:
        avaliar_sustentabilidade_satelite(satelite)

    print("\n" + "=" * 60)
    print("\t\tAUDITORIA DE FIM DE VIDA CONCLUÍDA")
    print("=" * 60 + "\n")