import random

NUM_ALTITUDES = 3
NUM_GRAUS = 360
MARGEM_SEGURANCA = 2

def lancamento():
    def criar_matriz_espacial():
        return [[0 for _ in range(NUM_GRAUS)] for _ in range(NUM_ALTITUDES)]

    def verificar_espaco(espaco, altitude, angulo_desejado):
        for i in range(-MARGEM_SEGURANCA, MARGEM_SEGURANCA + 1):
            angulo_verificar = (angulo_desejado + i) % 360
            if espaco[altitude][angulo_verificar] == 1:
                return False, angulo_verificar
        return True, None

    def gerar_lixo_espacial(espaco, quantidade):
        print(f"\n--- Existem {quantidade} satélites/objetos pelas órbitas de lançamento ---")
        sucessos = 0
        tentativas = 0
        limite_tentativas = quantidade * 10

        while sucessos < quantidade and tentativas < limite_tentativas:
            alt_aleatoria = random.randint(0, NUM_ALTITUDES - 1)
            ang_aleatorio = random.randint(0, NUM_GRAUS - 1)

            livre, _ = verificar_espaco(espaco, alt_aleatoria, ang_aleatorio)

            if livre:
                espaco[alt_aleatoria][ang_aleatorio] = 1
                sucessos += 1

            tentativas += 1

        print(f"Analisando, {sucessos} satélites/objetos na órbita.\n")

    def lancar_satelite(espaco, nome, altitude, angulo):
        if altitude >= len(espaco):
            print("Erro: Altitude fora de alcance.")
            return

        livre, angulo_conflito = verificar_espaco(espaco, altitude, angulo)

        if livre:
            espaco[altitude][angulo] = 1
            print(f"SUCESSO: Satélite '{nome}' posicionado na altitude {altitude}, ângulo {angulo}°.")
            print(f"Nem um outro satelite na zona de perigo")
        else:
            print(f"ALERTA DE COLISÃO! Lançamento do '{nome}' abortado.")
            print(f"   Motivo: Objeto detectado na zona de segurança (ângulo {angulo_conflito}°).")
            print(f"'{nome}' iria bater com outro Satélite.")

    minha_orbita = criar_matriz_espacial()

    gerar_lixo_espacial(minha_orbita, 50)

    lancar_satelite(minha_orbita, "Satélite FIAP", altitude=1, angulo=90)
    lancar_satelite(minha_orbita, "Satélite DEVS", altitude=2, angulo=270)