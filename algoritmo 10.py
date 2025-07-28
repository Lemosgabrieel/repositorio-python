altura = float(input("Digite a altura: "))
sexo = input("Digite o sexo (M/F): ")

if sexo.lower() == 'm':
    peso_ideal = (72.7 * altura) - 58
elif sexo.lower() == 'f':
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = 0
    print("Sexo inválido. Por favor, digite 'M' para masculino ou 'F' para feminino.")
print(f"O peso ideal é: {peso_ideal:.2f} kg")
