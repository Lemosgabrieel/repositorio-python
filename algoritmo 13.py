n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))

q1 = n1 * n1
q2 = n2 * n2
q3 = n3 * n3
q4 = n4 * n4

if(q3 >= 1000):
    print("O quadrado do terceiro número é maior ou igual a 1000.")
else:
    print("n1: {0}, quadrado: {1}".format(n1, q1))
    print("n2: {0}, quadrado: {1}".format(n2, q2))
    print("n3: {0}, quadrado: {1}".format(n3, q3))
    print("n4: {0}, quadrado: {1}".format(n4, q4))
