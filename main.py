import time
import MapeamentoDaOrbita
import Lancamento
import TrocarOrbita
import ClimaEspacial
import Sustentabilidade

def exibir_menu():
    print("\n" + "=" * 55)
    print("SISTEMA DE GERENCIAMENTO AEROESPACIAL (GS - 1ESPY)")
    print("=" * 55)
    print("  [ 1 ] - Descrição da Solução Proposta")
    print("  [ 2 ] - Simular Lançamento de Satélite")
    print("  [ 3 ] - Sistema Anticolisão (Trocar Órbita)")
    print("  [ 4 ] - Monitoramento de Clima Espacial (Safe Mode)")
    print("  [ 5 ] - Auditoria de Sustentabilidade (Lixo Espacial)")
    print("  [ 6 ] - Mapeamento das Órbitas (Relatório TLE)")
    print("  [ 0 ] - Sair do Sistema")
    print("-" * 55)

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção válida (0 a 6): ").strip()

        if opcao == '1':
            print("\n" + "=" * 68)
            print("A Flyspace é uma startup de Space Tech focada na gestão autônoma")
            print("do tráfego orbital. Nosso sistema processa dados TLE em tempo real,")
            print("lança satélites com segurança, previne colisões espaciais através")
            print("de manobras de desvio, mitiga lixo espacial com desorbitagem")
            print("e protege frotas contra tempestades de radiação solar.")
            print("=" * 68 + "\n")
            time.sleep(2.5)

        elif opcao == '2':
            print("\n>> Iniciando Módulo de Lançamento...")
            time.sleep(1)
            Lancamento.lancamento()

        elif opcao == '3':
            print("\n>> Iniciando Módulo de Troca de Órbita...")
            time.sleep(1)
            TrocarOrbita.executar_sistema_geral_anticolisao(TrocarOrbita.lista_de_satelites_proprios)

        elif opcao == '4':
            print("\n>> Iniciando Módulo de Clima Espacial...")
            time.sleep(1)
            ClimaEspacial.gerenciar_clima_espacial_frota(ClimaEspacial.lista_de_satelites_proprios)

        elif opcao == '5':
            print("\n>> Iniciando Módulo de Sustentabilidade...")
            time.sleep(1)
            Sustentabilidade.executar_auditoria_ambiental_espacial(Sustentabilidade.lista_de_satelites_proprios)

        elif opcao == '6':
            print("\n>> Iniciando Mapeamento da Órbita...")
            time.sleep(1)
            MapeamentoDaOrbita.mapeamentoDaOrbita()

        elif opcao == '0':
            print("\n>> Encerrando o sistema da FlySpace. Até logo!\n")
            break
        else:
            print("\nERRO: Entrada inválida! Por favor, digite apenas números entre 0 e 6.")
            time.sleep(1.5)

if __name__ == "__main__":
    main()