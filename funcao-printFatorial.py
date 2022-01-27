def calculaFatorial(n):
    nFat = 1
    while n > 0:
        nFat = nFat * n
        n -= 1
    return nFat


def informaNumero():
    n = 0
    while n >= 0:
        n = int(input("informe um numero inteiro: "))
        if n < 0:
            print("Digite um valor positivo.\n"
              "Tchau.")
            break
        auxN = calculaFatorial(n)
        print(auxN)

informaNumero()

    
