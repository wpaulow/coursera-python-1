def informa_numero():

    n = 0

    while n < 1:
        try:
            n = int(input("Me informe um número inteiro positivo: "))
        except:
            print("Você não me informou um número. Tente novamente.")

    return n


def eh_hipotenusa(n):
    
    if n % 17 == 0:
        return True
    elif n % 13 == 0:
        return True
    elif n % 5 == 0:
        return True
    else:
        return False
    


def soma_hipotenusas(n):
    somaHipotenusa = 0
    
    while n >= 5:
        hipotenusa = eh_hipotenusa(n)
        if hipotenusa == True:
            somaHipotenusa += n
        n -= 1
        
    return somaHipotenusa

print(soma_hipotenusas(informa_numero()))

