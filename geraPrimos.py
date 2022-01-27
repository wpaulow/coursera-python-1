def pegaNumero():

    n = 0

    while n <= 0:
        try:
            n = int(input("Informe o número limite da lista de números primos que você que você quer: "))
        except:
            print("Ou você não informou um número ou não informou um número inteiro.\n"
                  "Por favor, tente novamente.\n")
        if n <= 0:
            print("Você informou um número menor ou igual a zero.\n"
                  "Por favor, tente novamente.\n")

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



def retornaPrimos(primoMaximo):

    primos = []

    cont = 2
    
    while True:
        if primalidade(cont):
            primos.append(cont)
        if cont >= primoMaximo:
            break
        cont += 1

    return primos


primos = retornaPrimos(pegaNumero())
print(primos)

print("Só um pedaço da lista primos:")

print("da posição 3 à 8: ", primos[2:7], "\n") # Aqui o Python está mandando uma nova lista, formada a partir da primeira, e mantendo aquela incólume

comecoPrimos = primos[:12] # o mesmo que primos[0:12]
finalPrimos = primos[12:] # o mesmo que primos[12:25] (uma vez que len(primos) = 25)

print(comecoPrimos)
print(finalPrimos)

fakeNews = primos

print("TESTE:\t FAKE NEWS aponta para ORIGINAL?\t", fakeNews is primos)

def clonaLista(lista):

    listaClone = []
    for objeto in lista:
        listaClone.append(objeto)

    return listaClone

clonePrimos = clonaLista(primos)

print("TESTE CLONE... ", clonePrimos)
print("TESTE:\t CLONE aponta para ORIGINAL?\t", primos is clonePrimos)

print("---------------------------------------------------------------------------------\n")
print("um jeito ainda mais fácil de clonar uma lista:\n")

cloneLigeiro = primos[:] # retorna um clone de primos em cloneLigeiro




















