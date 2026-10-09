try:
    quantidade_alunos = int(input("Quantos alunos existem na turma? "))

    if quantidade_alunos <= 0:
        print("A quantidade de alunos deve ser maior que zero.")
    else:
        notas = []

        for i in range(quantidade_alunos):
            while True:
                try:
                    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("Erro: A nota deve estar entre 0 e 10.")
                except ValueError:
                    print("Erro: Entrada inválida. Digite apenas números.")

        media = sum(notas) / len(notas)
        print(f"\nA média exata da turma é: {media:.2f}")

except ValueError:
    print("Erro: Digite um número inteiro válido para a quantidade de alunos.")
