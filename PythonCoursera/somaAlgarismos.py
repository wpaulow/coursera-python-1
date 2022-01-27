x = int(input("Digite um número inteiro:"))
soma = 0

while x != 0:
    a = x % 10
    soma += a
    x = x // 10

print(soma)
