n = int(input("Digite um número inteiro:"))

count = 1
divisores = 0

while count <= n:
    if n % count == 0:
        divisores += 1
    count += 1

if divisores == 2:
    print("primo")
else:
    print("não primo")
    
