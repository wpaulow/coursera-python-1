def informaNumero():

    n = -1

    while n < 0:
        try:
            n = int(input("Me informe um número: "))
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
    
"""
########## Essa foi a solução abordada pelo professor do curso
########## que não aborda o número 2 como sendo primo.
def ePrimo(x):

    fator = 2
    while x % fator != 0 and fator <= x/2: #se não encontrar um número que fatore ele até a sua primeira metade, não será na segunda metade que irá encontrar.
        fator += 1
    if x % fator == 0:
        return False
    else:
        return True
"""

def main():

    count = 1
    while count <= 10:
        bulinha = primalidade(informaNumero())
      
        if bulinha == True:
            print("É primo!!! É primo!!!! É do Braaasil!!!")
            print()
        else:
            print("Não. Não é Primo. É apenas um número qualquer.\n"
                  "Um número qualquer.")
            print()
        count += 1

main()
    
