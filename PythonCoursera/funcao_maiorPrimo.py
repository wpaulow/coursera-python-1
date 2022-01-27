def ePrimo(n):
    count = 1
    divisores = 0

    while count <= n:
        if n % count == 0:
            divisores += 1
        count += 1

    if divisores == 2:
        return True


def maior_primo(a):
    if ePrimo(a):
        return a
    else:
        aux = a - 1
        while (not ePrimo(aux)):
            aux -= 1
        return aux
        
        
