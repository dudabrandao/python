numeros= []

p = int(input("Quantas vezes você irá testar o programa?\n"))

for i in range(p):
    x = int(input("Digite algum número: \n"))
    if x == 0:
        break
    elif x not in numeros:
        numeros.append(x)
numeros.sort()
print(numeros)