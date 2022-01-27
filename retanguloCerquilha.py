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

def imprimeRetanguloPreenchido(x, y):
    amiguinha = 1
    amigona = 1
    while amigona <= y:
        while amiguinha <= x:
            print("#", end="")
            amiguinha += 1
        amigona += 1
        amiguinha = 1
        print()

a = larguraRetangulo()
b = alturaRetangulo()

imprimeRetanguloPreenchido(a,b)
    
