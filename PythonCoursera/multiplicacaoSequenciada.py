print("Digite uma sequência de valores terminada por 1:")

valor = int(input("Digite um valor a ser multiplicado:"))

produto = valor

while valor != 1:
    valor = int(input("Digite um valor a ser multiplicado:"))
    produto *= valor

print("O produto dos valores digitados é:", produto)
