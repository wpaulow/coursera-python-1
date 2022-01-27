import math

print("Vamos resolver uma Equação do Segundo Grau?")
print("Foda-se. Essa pergunta é retórica. Não me importa se você quer ou não resolver")
print("Eu vou resolver esta merda. Me informe os coeficientes agora, infeliz!")

a = float(input("Informe o valor de a:"))
b = float(input("Informe o valor de b:"))
c = float(input("Informe o valor de c:"))

delta = b**2 - 4 * a * c

if delta > 0:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    if x1 < x2:
        print("as raízes da equação são %5.2f e %5.2f" % (x1,x2))
    else:
        print("as raízes da equação são %5.2f e %5.2f" % (x2,x1))
elif delta == 0:
    x = -b/(2*a)
    print("a raiz desta equação é" , x)
else:
    print("esta equação não possui raízes reais.")
