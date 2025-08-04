maior = -999
menor = 999
soma = 0

for n in range(1, 11):
    valor = int(input("Informe um valor: "))
    if valor > 0:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
        soma = soma + valor
    else:
        valor = int(input("Informe um valor: "))
media = soma / 10
print("o maior numero é {0}". format(maior))
print("o menor numero é {0}". format(menor))
print("a media dos numeros é {0}". format(media))
