try:
    limite = int(input("Digite um limite N: "))
    for i in range(1, limite + 1):
        if i % 2 == 0:
            print(i)
except ValueError:
    print("Erro: Digite apenas números inteiros.")

