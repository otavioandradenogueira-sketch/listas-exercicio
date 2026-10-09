while True:
    try:
        nota = float(input("Digite uma nota de 0 a 10: "))
        if 0 <= nota <= 10:
            print(f"Nota {nota} validada com sucesso!")
            break
        else:
            print("Erro: A nota deve estar entre 0 e 10. Tente novamente.")
    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números.")
