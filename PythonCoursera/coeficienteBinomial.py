def fatorial(a):
    fat = 1
    while a > 1:
        fat = fat * a
        a = a - 1
    return fat


def coefBinomial(m, n):
    return fatorial(m)/(fatorial(n)*fatorial(m-n))


'''
n = int(input("Digite o valor de n:"))
k = int(input("Digite o valor de k:"))

'''

print(coefBinomial(4,2))
print(coefBinomial(5,3))
print(coefBinomial(10,4))
print(coefBinomial(9,8))


print(fatorial(0))
