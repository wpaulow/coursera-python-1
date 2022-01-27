import math

x1 = int(input("Informe o valor de x1:"))
y1 = int(input("Informe o valor de y1:"))
x2 = int(input("Informe o valor de x2:"))
y2 = int(input("Informe o valor de y2:"))

dAB = math.sqrt((x2-x1)**2 + (y2-y1)**2)

if dAB >= 10:
    print("longe")
else:
    print("perto")
