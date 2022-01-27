print("Digite uma sequência de valores terminada por 0 (zero):")

valor = int(input("Digite um valor a ser somado:"))

soma = valor

while valor != 0:
    valor = int(input("Digite um valor a ser somado:"))
    soma += valor

print("A soma dos valores digitados é:", soma)
