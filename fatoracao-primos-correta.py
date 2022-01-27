print("----------------------------------------------\n"
      "----------------------------------------------\n"
      "----------------------------------------------\n")
print("Dado um número inteiro n, onde n > 1, imprimir\n"
      "sua decomposição em fatores primos, indicando\n"
      "também a multiplicidade de cada fator.")
print("----------------------------------------------\n"
      "----------------------------------------------\n"
      "----------------------------------------------\n")

def informaNumero():
    n = 1

    while n <= 1:
        try:
            n = int(input("Informe um número inteiro maior que 1, por favor: "))
            print("Você informou o número:\n\t\t %d." % n)
        except:
            print("Isso não se parece com um número. Tente novamente.\n")

    return n

def fatoraEmPrimos(n):
    fator = 2
    multipli = 0

    while n != 1:
        while n % fator == 0:
            multipli += 1
            n = n / fator
        if multipli > 0:
            print("fator: %d;\t multiplicidade = %d;\t %d^%d" % (fator, multipli, fator, multipli))
        fator += 1
        multipli = 0

fatoraEmPrimos(informaNumero())

"""
A função desse programa é descobrir a quantidade de números primos
que um número possuí em si.
"""



































