def pegaLista():

    n = 1
    listaNumeros = []

    while n != 0:
        try:
            n = int(input("Me informe uma lista de números inteiros e digite 0 quando quiser parar: "))
            listaNumeros.append(n)
        except:
            print("Você não me informou um número. Tente novamente.")
        
    return listaNumeros

def exibeLista():

    print("-----------------------------------------------------------------------------------------\n")

    lista = pegaLista()

    ultimoIndice = len(lista)-1

    print("-----------------------------------------------------------------------------------------\n"*5) # isso é poderoso. muito poderoso
    

    while ultimoIndice >= 0:
        
        print(lista[ultimoIndice])
        ultimoIndice -= 1

def exibeLista2():

    print("-----------------------------------------------------------------------------------------\n")
    print("------------------------------------Lista Doida--------------------------------------------")
    print("(feita com um for muito doido)")
    
    lista = pegaLista()

    tamanhoLista = len(lista)-1

    tamanhoOposto = len(lista) * -1

    print(tamanhoLista, tamanhoOposto)
    print("TESTE")

    for i in range(-1, tamanhoOposto-1, -1): # esse tamanhoOposto-1 foi uma forma de "aumentar" o valor da variável em 1, já que ela era negativa, de modo que o for conseguisse abarcar a condição do último índice da lista de trás para frente
        print("Teste ", i)
        print(lista[i])
        print("teste tamanho oposto ", tamanhoOposto)



exibeLista()



exibeLista2()

    










