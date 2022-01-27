n = int(input("Digite o valor de n:"))

count = 1

while count <= n*2:
    if count % 2 != 0:
        print(count)
    count += 1
