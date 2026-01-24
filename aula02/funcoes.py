import json


database = []


def finalizar_chamado():
    print("\n--- Finalizar Chamado ---")
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

    from datetime import datetime
    agora = datetime.now()
    timestamp = agora.timestamp()
    data = datetime.fromtimestamp(timestamp)
    print(data)

    chamado = {
        "lab": laboratorio,
        "descricao": descricao,
        "prioridade": prioridade,
        "status": "Aberto",
        "data": data.strftime("%d/%m/%Y %H:%M:%S")
    } 

    database.append(chamado)
    print(" Chamado registrado com sucesso!")
    return True

def listar_chamados():
    for c in database: 
        print("\n--- TODOS OS CHAMADOS ---") 
        print(f"{c['data']} {c['status']} Lab: {c['lab']} - {c['descricao']} (Prioridade: {c['prioridade']})")
        return True

def exportar_chamados():
    with open ("chamados.txt", "a") as arquivo:
            json.dump(database, arquivo, indent=4)         
    print("chamados exportados com sucesso para 'chamados.txt'!")
    return True

def importar_chamados():
    with open ("chamados.txt", "r") as arquivo:
        dados = json.load(arquivo)
        database.extend(dados)
    print("Chamados importados com sucesso de 'chamados.txt'!")
    return True
