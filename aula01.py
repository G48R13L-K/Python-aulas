nome = input("Qual é o nome do aluno?")
disciplina = input("Qual é a disciplina?")
nomeProfessor = input("Qual é o nome do professor?")
notas = []
i=0
for i in i+1 in range(4):
    nota = float(input("Digite a nota: "))
    if (0 <= nota <= 10):
        notas.append(nota)
    else:
        print("Nota inválida. Digite uma nota entre 0 e 10.")
        i -= 1
       

media = sum(notas) / len(notas)
print(f"A média do aluno {nome} na disciplina {disciplina} do professor {nomeProfessor} é {media:.2f}")