nome = input("digite seu nome: ")
senha = input("digite sua senha: ")

while nome == senha:
    print("erro, a senha não pode ser igual ao nome")
    senha = input("digite sua senha: ")
    nome = input("digite seu nome: ")
    