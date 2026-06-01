import time

LIMITE_MINIMO_COMBUSTIVEL_PORCENTO = 5.0
LIMITE_ALTITUDE_LEO_KM = 2000.0

lista_de_satelites_proprios = [
    {"identificador": "FLY-SUSTAIN-1", "altitude_atual": 550, "combustivel": 65.0, "ciclo_vida": "Ativo"},
    {"identificador": "FLY-SUSTAIN-2", "altitude_atual": 720, "combustivel": 3.2, "ciclo_vida": "Ativo"},
    {"identificador": "FLY-SUSTAIN-3", "altitude_atual": 2200, "combustivel": 4.1, "ciclo_vida": "Ativo"},
]

def avaliar_sustentabilidade_satelite(satelite):
    print(f"\nANÁLISE DE CICLO DE VIDA: {satelite['identificador']}")
    print(f"Altitude: {satelite['altitude_atual']} km | Combustível: {satelite['combustivel']}%")
    time.sleep(0.8)

    if satelite["combustivel"] <= LIMITE_MINIMO_COMBUSTIVEL_PORCENTO:
        print(f"Alerta de Fim de Vida Utilizado! Combustível abaixo de {LIMITE_MINIMO_COMBUSTIVEL_PORCENTO}%.")
        print("Ativando Diretriz Flyspace de mitigação de detritos...")
        time.sleep(1.0)

        if satelite["altitude_atual"] <= LIMITE_ALTITUDE_LEO_KM:
            satelite["ciclo_vida"] = "Desorbitado (Queima Atmosférica)"
            print("PROTOCOLO REENTRADA ATIVADO:")
            print(f"  -> Acionando propulsores para reduzir altitude de {satelite['altitude_atual']} km.")
            print("  -> Destino: Reentrada forçada e desintegração segura na atmosfera terrestre.")
        else:
            satelite["ciclo_vida"] = "Desorbitado (Órbita Cemitério)"
            print("PROTOCOLO GRAVEYARD ORBIT ACTIVATED:")
            print(f"  -> Utilizando última reserva de empuxo para elevar a altitude para fora das rotas ativas.")
            print("  -> Destino: Estabilização na Órbita Cemitério (Graveyard Orbit) de segurança.")

        print(f"  -> Novo Status do Satélite: {satelite['ciclo_vida']}")
    else:
        print("Satélite saudável. Autonomia garantida para continuar a missão.")

    print("-" * 60)
    time.sleep(0.5)

def executar_auditoria_ambiental_espacial(lista_de_satelites):
    print("\n" + "=" * 60)
    print("\tFLYSPACE - SISTEMA DE SUSTENTABILIDADE ORBITAL")
    print("=" * 60)
    time.sleep(1.0)

    for satelite in lista_de_satelites:
        avaliar_sustentabilidade_satelite(satelite)

    print("\n" + "=" * 60)
    print("\t\tAUDITORIA DE LIXO ESPACIAL CONCLUÍDA")
    print("=" * 60 + "\n")