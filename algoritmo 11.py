p = float(input("informe o peso dos peixes: "))

if p > 50: 
    m = (p - 50) * 4
    e = "excesso de peso"
    print("voce devera pagar {:.2f} reais de multa".format(m))
else:
    m = 0
    e = "dentro do limite de peso"
    print("você está dentro do limite de peso, sem multa")