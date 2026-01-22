nome = input("Qual é o nome do aluno?")
disciplina = input("Qual é a disciplina?")
nomeProfessor = input("Qual é o nome do professor?")
notas = []
i = 0
while len(notas) < 4:
    try:
        nota = float(input("Digite a nota:"))
        if (0 <= nota and nota <= 10):
            notas.append(nota)
            i += 1
        else:
            print("Nota inválida. Digite uma nota entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
    
media = sum(notas) / len(notas)
print(f"A média do aluno {nome} na disciplina {disciplina} do professor {nomeProfessor} é {media:.2f}")