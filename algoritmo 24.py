#variaveis 
vetor1 = []
vetor2 = []
soma = []
#entrada/processamento 
for n in range(0, 10):
    n1 = int(input("informe o valor para o primeiro vetor: "))
    vetor1.append(n1)
    n2 = int(input("informe o valor para o segundo vetor: "))
    vetor2.append(n2)
    soma.append(n1 + n2)
for n in soma:
    print(n)
