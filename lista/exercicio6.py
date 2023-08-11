numeros = []

while True:
    numeros.append(int(input('digite um número ou zero para encerrar: ')))
    if 0 in numeros:
        break

quantidade = len(numeros)
decrescente = sorted(numeros, reverse=True)
if 5 in numeros:
    print('o número 5 está na lista')

print('quantidade de números: ', quantidade)
print('ordem decrescente: ', decrescente)