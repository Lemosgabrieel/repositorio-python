c = int(input("digite o codigo do operario: "))
n = float(input("digite o numero de horas trabalhadas: "))
valor_hora = 10.00
valor_hora_excedente = 20.00
e = 0

if n > 50: 
    e = (n - 50) * valor_hora_excedente
    salario = (50 * valor_hora) 
    print("salario total: R$ %.2f" % (salario + e))
    print("valor excedente: R$ %.2f" % e)
else:
    salario = n * valor_hora
    print("salario total: R$ %.2f" % salario)
    print("valor excedente: R$ 0.00")