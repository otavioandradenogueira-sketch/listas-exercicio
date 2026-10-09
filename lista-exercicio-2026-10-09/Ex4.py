soma = 0

while True:
    try:
        numero = float(input("Digite um número (ou 0 para parar): "))
        if numero == 0:
            break
        soma += numero
    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números.")

print(f"A soma total é: {soma}")
