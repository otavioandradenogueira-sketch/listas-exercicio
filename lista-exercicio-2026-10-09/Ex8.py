try:
    numero = int(input("Digite um número inteiro: "))
    
    if numero < 2:
        eh_primo = False
    else:
        eh_primo = True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                eh_primo = False
                break

    if eh_primo:
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")
        
except ValueError:
    print("Erro: Digite apenas números inteiros.")
