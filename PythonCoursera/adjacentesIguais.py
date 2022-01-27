iguais = False

valor = int(input("Digite um número com 4 dígitos ou mais:"))

valorOriginal = valor

while valor != 0 and not iguais:
    a = valor % 10
    valor = valor // 10
    b = valor % 10
    print(valor)
    if a == b:
        iguais = True
        print(valorOriginal,"possuí números adjacentes iguais")

if valor == 0:
    print(valorOriginal, "não possuí números adjacentes iguais")
