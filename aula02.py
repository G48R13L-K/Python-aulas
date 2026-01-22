database = []  # Lista para armazenar os chamados

def finalizar_chamado(laboratorio):
    for chamado in database:
        if chamado["lab"] == laboratorio and chamado["status"] == "Aberto":
            chamado["status"] = "Finalizado"
            print(" Chamado finalizado com sucesso!")
            return True
        print(" Chamado não encontrado ou já finalizado.")
        return False
    print(" Nenhum chamado aberto encontrado para esse laboratório.")
    
def abrir_chamado(laboratorio, descricao, prioridade):
    # Validação simples
    if prioridade < 1 or prioridade > 10:
        print("Erro: A prioridade deve ser entre 1 e 10.")
        return False
    # Criando o registro (Dicionário)
    chamado = {
        "lab": laboratorio,
        "descricao": descricao,
        "prioridade": prioridade,
        "status": "Aberto"
    } 

    database.append(chamado)
    print(" Chamado registrado com sucesso!")
    return True

while True:
    print("\n--- HELP DESK TÉCNICO ---") 
    print("1. Novo Chamado") 
    print("2. Listar Chamados")
    print("3. Finalizar Chamado") 
    print("0. Sair") 
    opcao = input("Escolha uma opção: ") 
    if opcao == "1":
        l = input("Laboratório: ") 
        d = input("Descrição do problema: ")
        p = int(input("Prioridade (1-10): "))
        abrir_chamado(l, d, p) 
    elif opcao == "2": 
        print("\n--- TODOS OS CHAMADOS ---") 
        for c in database: 
            print(f"[{c['status']}] Lab: {c['lab']} - {c['descricao']} (Prioridade: {c['prioridade']})") 
    elif opcao == "0":
        print("Desligando sistema...")
        break
    elif opcao =="3":
        print("\n--- Finalizar Chamado ---")
        lab = input("Laboratório do chamado a finalizar: ")
        finalizar_chamado(lab)


