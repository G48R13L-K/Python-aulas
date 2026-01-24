from funcoes import *

while True:
    print("\n--- HELP DESK TÉCNICO ---") 
    print("1. Novo Chamado") 
    print("2. Listar Chamados")
    print("3. Finalizar Chamado")
    print("4. Exportar Chamados")
    print("5. Importar Chamados") 
    print("0. Sair") 

    opcao = int(input("Escolha uma opção: "))
    match opcao: 
        case 1:
            l = input("Laboratório: ") 
            d = input("Descrição do problema: ")
            p = int(input("Prioridade (1-10): "))
            abrir_chamado(l, d, p) 
        case 2: 
            listar_chamados() 
        case 3:
            print("\n--- Finalizar Chamado ---")
            finalizar_chamado()
        case 4:
            exportar_chamados()
        case 5:
            importar_chamados()
        case 0:
            print("Desligando sistema...")
            break
        case _:
            print("Opção inválida. Tente novamente.")


