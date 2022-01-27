n = int(input("Digite o valor de n:"))

if n > 0:
    nFat = 1
    count = n
    while count > 0:
        nFat = nFat * count
        count = count - 1
    print(nFat)

elif n == 0:
    print("1")

else:
    print("Digite um valor positivo.")
