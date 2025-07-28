vgh = float(input("Digite o valor de ganho por hora: "))
nht = int(input("Digite o número de horas trabalhadas no mês: "))

salario = vgh * nht

print("O salário do funcionário é: R$ {:.2f}".format(salario))
