numero = int(input("Digite um número: "))

if numero % 2 == 0:
    if numero > 0:
        print("O número é positivo e par.")
    else: 
        print("O número é negativo e par.")
else:
    if numero > 0:
        print("O número é positivo e ímpar.")
    else: 
        print("O número é negativo e ímpar.")