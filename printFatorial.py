n = 0
while n >= 0:
    n = int(input("Informe um número inteiro: "))

    if n >= 0:
        nFat = 1
        while n > 0:
            nFat = nFat * n
            n -= 1
        print(nFat)
    else:
        print("Digite um valor positivo.\n"
              "Tchau.")

