def pega_lista():

    n = 1
    listaNumeros = []

    while n != 0:
        try:
            n = int(input("Me informe uma lista de números inteiros e digite 0 quando quiser parar: "))
            listaNumeros.append(n)
        except:
            print("Você não me informou um número. Tente novamente.")

    listaNumeros.remove(0)
    
    return listaNumeros



def exibe_lista(lista):

    tamanhoLista = len(lista)-1

    tamanhoOposto = len(lista) * -1

    for i in range(-1, tamanhoOposto-1, -1):
        print(lista[i])


lista = pega_lista()

exibe_lista(lista)







