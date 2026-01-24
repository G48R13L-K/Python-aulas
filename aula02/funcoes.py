database = []


def finalizar_chamado():
    id_chamado = int(input("Qual o Id do chamado a finalizar: "))
    if 0 <= id_chamado < len(database):
        database[id_chamado]["status"] = "Finalizado"
        print(f" Chamado {id_chamado} finalizado com sucesso!")
        return True
    else:
        print(" Id de chamado inválido.")
    

def abrir_chamado(laboratorio, descricao, prioridade):
    # Validação simples
    if prioridade < 1 or prioridade > 10:
        print("Erro: A prioridade deve ser entre 1 e 10.")
        return True
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

def listar_chamados():
    for c in database: 
        print("\n--- TODOS OS CHAMADOS ---") 
        print(f"[{c['status']}] Lab: {c['lab']} - {c['descricao']} (Prioridade: {c['prioridade']})")
        return True
