try:
    q = int(input("Digite a quantidade de termos (Q): "))

    if q <= 0:
        print("Por favor, digite um número maior que zero.")
    else:
        a, b = 0, 1
        for _ in range(q):
            print(a, end=" ")
            a, b = b, a + b
        print()
        
except ValueError:
    print("Erro: Digite apenas números inteiros.")
