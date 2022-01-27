def min_max(temperaturas):
    print("A menor temperatura do mês foi: ", minima(temperaturas), "C.")
    print("A menor temperatura do mês foi: ", maxima(temperaturas), "C.")


def minima(temps):
    mini = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] < mini:
            mini = temps[i]
        i += 1
    return mini


def maxima(temps):
    maxi = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] > maxi:
            maxi = temps[i]
        i += 1
    return maxi


def teste_minima(temp, valor_esperado):
    valor_calculado = minima(temp)
    if valor_calculado != valor_esperado:
        print("Valor errado para array ", temp)
        print("Valor esperado: ", valor_esperado, ". Valor calculado: ", valor_calculado)


def teste_maxima(temp, valor_esperado):
    valor_calculado = maxima(temp)
    if valor_calculado != valor_esperado:
        print("Valor errado para array ", temp)
        print("Valor esperado: ", valor_esperado, ". Valor calculado: ", valor_calculado)
        

def testa_minima():
    print("Iniciando os testes")
    
    testes = [[[0], 0], [[0, 0, 0, 0, 0, 0], 0], [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0],
              [[30, 27, 25, 26, 29, 31, 32, 33, 30, 29, 24, 26, 30, 27, 24, 25, 26, 24, 22, 23], 22],
              [[-15, -12, 0, 20, 30], -15]]

    for i in testes:
        teste_minima(temp = i[0], valor_esperado = i[1])
     
    print("Finalizando os testes")



def testa_maxima():
    print("Iniciando os testes")
    
    testes = [[[0], 0], [[0, 0, 0, 0, 0, 0], 0], [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10],
              [[30, 27, 25, 26, 29, 31, 32, 33, 30, 29, 24, 26, 30, 27, 24, 25, 26, 24, 22, 23], 33],
              [[-15, -12, 0, 20, 30], 30]]
    
    for i in testes:
        teste_maxima(temp = i[0], valor_esperado = i[1])
       
    print("Finalizando os testes")
    
