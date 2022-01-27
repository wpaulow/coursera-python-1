"""
i = 0
while i < 3:
  j = 0
  while j < 3:
    print(3 * i + j + 1, end=" ")#expressão
    j = j + 1
  i = i + 1

######## Saída: 1 2 3 4 5 6 7 8 9


"""




"""
n = int(input("Digite o valor de n:"))

if n > 0:
    nFat = 1
    count = n
    while count > 0:
        nFat = nFat * count
        count = count - 1
    print(nFat)

elif n == 0:
    print("1")

else:
    print("Digite um valor positivo.")


"""

for p in [True,False]:
    for q in [True,False]:
        if p and not q:
            print(p,'-->',q,'=',False)
        else:
            print(p,'-->',q,'=',True)
