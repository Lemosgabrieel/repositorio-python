indice = float(input("Digite o índice de poluição: "))

if indice >= 0.3 and indice < 0.4:
    print("Atenção: industrias do setor 1 devem ser notificadas.")
elif indice >= 0.4 and indice < 0.5:    
    print("Atenção: industrias do setor 1 e 2 devem ser notificadas.")
elif indice >= 0.5:
    print("Atenção: industrias do setor 1, 2 e 3 devem ser notificadas.")