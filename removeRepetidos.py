def remove_repetidos(lista):
##    listaOriginal = lista
##    print("Lista Original: ", listaOriginal)
    listaOrdenada = sorted(lista)
##    print("Lista Ordenada: ", listaOrdenada)
    listaBoa = []

    for i in listaOrdenada:
        for j in listaOrdenada:
            if i == j:
                if j not in listaBoa:
                    listaBoa.append(i)

    return listaBoa

##listaZuada = [2,4,4,2,2,3,3,1]
##listaZuada = [1, 2, 3, 3, 3, 4]
##lista = remove_repetidos(listaZuada)
##print("lista sem repetidos: ", lista)
        
