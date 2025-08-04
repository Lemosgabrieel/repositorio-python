#variaveis
maior = 0
#entrada 
n = int(input("informe um numero: "))
while n != 0:
    if n > maior:
        maior = n 
    n = int(input("informe um numero: "))
print("o maior número é {0}". format(maior))
