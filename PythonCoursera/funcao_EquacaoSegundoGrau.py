import math

def delta(a,b,c):
    return b**2 -4 * a * c


def bhaskara(a,b,c):
    if delta(a,b,c) < 0:
        print("esta equação não possui raízes reais.")
    elif delta(a,b,c) == 0:
        x = -b/(2*a)
        print("a raiz desta equação é" , x)
    else:
        x1 = (-b + math.sqrt(delta(a,b,c)))/(2*a)
        x2 = (-b - math.sqrt(delta(a,b,c)))/(2*a)
        if x1 < x2:
            print("as raízes da equação são %5.2f e %5.2f" % (x1,x2))
        else:
            print("as raízes da equação são %5.2f e %5.2f" % (x2,x1))


bhaskara(2,8,9)
bhaskara(9,8,2)
bhaskara(8,9,2)
bhaskara(2,5,3)
