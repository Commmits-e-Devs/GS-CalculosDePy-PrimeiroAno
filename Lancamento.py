import random
import time

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
        print(f"\n--- Gerando {quantidade} objetos/detritos nas órbitas de teste ---")
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
        print(f"[SIMULAÇÃO MATRICIAL] {sucessos} pontos ocupados na grade de tráfego.\n")

    def exibir_radar_orbital(espaco, altitude_alvo, angulo_alvo):
        print("\n--> VISUALIZAÇÃO GRÁFICA DO RADAR SETORIAL (ÂNGULOS NOMINAIS):")
        print("Altitude | " + " ".join(f"{a:02d}°" for a in range(angulo_alvo - 5, angulo_alvo + 6)))
        print("    " + "-" * 55)

        nomes_altitudes = ["Baixa (0)", "Média (1)", "Alta  (2)"]
        for alt in range(NUM_ALTITUDES):
            linha_visual = []
            for ang in range(angulo_alvo - 5, angulo_alvo + 6):
                ang_normalizado = ang % 360
                if alt == altitude_alvo and ang_normalizado == angulo_alvo:
                    linha_visual.append(" 🛰️ ")
                elif espaco[alt][ang_normalizado] == 1:
                    linha_visual.append(" 💥 ")
                else:
                    linha_visual.append("  . ")

            marcador = "=>" if alt == altitude_alvo else "  "
            print(f"{marcador} {nomes_altitudes[alt]} |" + "".join(linha_visual))
        print("Legenda: [ . Espaço Livre ]  [ Detrito/Ocupado ]  [ Seu Satélite ]\n")

    def lancar_satelite(espaco, nome, altitude, angulo):
        if altitude >= len(espaco):
            print("Erro: Altitude fora de alcance.")
            return

        print(f"Avaliando janela cinemática para '{nome}' em {angulo}°...")
        time.sleep(0.8)
        livre, angulo_conflito = verificar_espaco(espaco, altitude, angulo)

        if livre:
            espaco[altitude][angulo] = 1
            print(f"SUCESSO: Satélite '{nome}' posicionado de forma estável na grade.")
            print(f"Nenhum vetor de colisão detectado na zona de segurança de ±{MARGEM_SEGURANCA}°.")
            exibir_radar_orbital(espaco, altitude, angulo)
        else:
            print(f"ALERTA DE COLISÃO CRÍTICA! Missão do '{nome}' abortada de emergência.")
            print(f"Vetor interceptado no ângulo {angulo_conflito}° (Margem de segurança violada).")
            exibir_radar_orbital(espaco, altitude, angulo)

    minha_orbita = criar_matriz_espacial()
    gerar_lixo_espacial(minha_orbita, 45)

    lancar_satelite(minha_orbita, "Satélite FIAP", altitude=1, angulo=90)
    time.sleep(1.0)
    lancar_satelite(minha_orbita, "Satélite DEVS", altitude=2, angulo=270)