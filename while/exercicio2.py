soma = 0
qntpares = 0
while True:
    num = int(input('Digite um número: '))
    if num == 0:
        print(f'A soma dos números pares é: {soma}')
        break
    elif num %2 == 0:
        soma += num