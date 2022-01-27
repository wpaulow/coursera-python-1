"""
def pegaLista():

    n = 1
    lista = []
    
    while n != 0:
        try:
            n = int(input("Me informa uma lista de números inteiros e digite 0 quando quiser parar: "))
            lista.append(n)
        except:
            print("Você não me informou um número. Tente novamente.")

    return lista
"""

def maior_elemento(lista):

    listaOrdenada = sorted(lista)

    return listaOrdenada[-1]

##maior = maior_elemento(pegaLista())
##
##print(maior)
