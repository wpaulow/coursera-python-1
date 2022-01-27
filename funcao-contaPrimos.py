def informa_numero():

    n = 1

    while n < 2:
        try:
            n = int(input("Me informe um número maior ou igual a 2: "))
        except:
            print("Você não me informou um número. Tente novamente.")

    return n

def primalidade(n):

    count = 1
    divisores = 0

    while count <= n:
        if n % count == 0:
            divisores += 1
        count += 1

    if divisores == 2:
        return True
    if divisores > 2:
        return False

def n_primos(n):
    countPrimos = 0
    i = 2
    while i <= n:
        boolPrimo = primalidade(i)
        if boolPrimo == True:
            countPrimos += 1
        i += 1
    return countPrimos

print(n_primos(informa_numero()))


