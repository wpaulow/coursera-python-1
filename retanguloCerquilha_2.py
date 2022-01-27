def larguraRetangulo():

    n = 1

    while n <= 1:
        try:
            n = int(input("Me informe a largura do retângulo\n"
                          "maior ou igual a dois: "))
        except:
            print("Você não me informou um número. Tente novamente.")
    
    return n

def alturaRetangulo():

    n = 1

    while n <= 1:
        try:
            n = int(input("Me informe a altura do retângulo\n"
                          "maior ou igual a dois: "))
        except:
            print("Você não me informou um número. Tente novamente.")
    
    return n


def imprimeRetanguloVazio(x, y):
    xis = 1
    ypsy = 1
    while ypsy <= y:
        if ypsy == 1 or ypsy == y:
            while xis <= x:
                print("#", end="")
                xis += 1
            xis = 1
        else:
            while xis <= x:
                if xis == 1:
                    print("#", end=(x-2)*" ") #A charada está aqui
                if xis == x:
                    print("#", end="")
                xis += 1
            xis = 1
        ypsy += 1
        print()

a = larguraRetangulo()
b = alturaRetangulo()

imprimeRetanguloVazio(a,b)
