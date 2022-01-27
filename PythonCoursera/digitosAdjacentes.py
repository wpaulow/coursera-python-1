iguais = False

valor = int(input("Digite um número inteiro:"))

while valor != 0 and not iguais:
    a = valor % 10
    valor = valor // 10
    b = valor % 10
    if a == b:
        iguais = True
        print("sim")

if valor == 0:
    print("não")
