print("----------------------------------------------\n"
      "----------------------------------------------\n"
      "----------------------------------------------\n")
print("Dado um número inteiro n, onde n > 1, imprimir\n"
      "sua decomposição em fatores primos, indicando\n"
      "também a multiplicidade de cada fator.")
print("----------------------------------------------\n"
      "----------------------------------------------\n"
      "----------------------------------------------\n")
n = 1

while n <= 1:
    try:
        n = int(input("Informe um número inteiro maior que 1, por favor: "))
        print()
        print("Você informou o número:\n\t\t %d." % n)
        print()
    except:
        print("Isso não se parece com um número. Tente novamente.\n")

count2 = 0
count3 = 0
count5 = 0
"""
##################### ERRADA ##################################

NÃO funciona um número alto como por exemplo 457136254, pois o
while só prevê três divisões possíveis.
"""


nZero = n

bool2 = False
bool3 = False
bool5 = False

while n != 1:
    
    while n % 2 == 0:
        n0 = n
        n = n // 2
        count2 += 1 # contando a multiplicidade desse fator
        print("%d / 2 = %d." % (n0, n))
    if count2 > 0:
        bool2 = True 
        print()
        print("A multiplicidade do fator 2 é %d, ou seja, 2^%d.\n" %(count2, count2))
    
    while n % 3 == 0:
        n0 = n
        n = n // 3
        count3 += 1
        print("%d / 3 = %d." % (n0, n))
    if count3 > 0:
        bool3 = True
        print()
        print("A multiplicidade do fator 3 é %d, ou seja, 3^%d.\n" %(count3, count3))
    
    while n % 5 == 0:
        n0 = n
        n = n // 5
        count5 += 1
        print("%d / 5 = %d." % (n0, n))
    if count5 > 0:
        bool5 = True
        print()
        print("A multiplicidade do fator 5 é %d, ou seja, 5^%d.\n" %(count5, count5))

    if not bool5 and bool2 and bool3:
        print()
        print("---------------------------------------------")
        print("%d equivale a 2^%d * 3^%d." % (nZero, count2, count3))
        print()
        print("---------------------------------------------")
    elif not bool3 and bool2 and bool5:
        print()
        print("---------------------------------------------")
        print("%d equivale a 2^%d * 5^%d." % (nZero, count2, count5))
        print()
        print("---------------------------------------------")
    elif not bool2 and bool3 and bool5:
        print()
        print("---------------------------------------------")
        print("%d equivale a 3^%d * 5^%d." % (nZero, count3, count5))
        print()
        print("---------------------------------------------")
    elif bool2 and bool3 and bool5:
        print()
        print("---------------------------------------------")
        print()
        print("%d equivale a 2^%d * 3^%d * 5^%d." % (nZero, count2, count3, count5))
        print()
        print("---------------------------------------------")
    else:
        print()
        print("---------------------------------------------")
        











