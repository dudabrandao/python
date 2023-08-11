num = 0
num2 = 0

while True:
    num = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))
    calcular = int(input('Qual operação deseja escolher?\nAdição(1)\nSubtração(2)\nMultiplicação(3)\nDivisão(4)\nSair do programa(5)\n'))
    if calcular == 1:
        adicao = num + num2
        print(f'Sua operação escolhida foi adição. Esse é o resultado: {adicao}')
    elif calcular == 2:
        sub = num - num2
        print(f'Sua operação escolhida foi subtração. Esse é o resultado: {sub}')
    elif calcular == 3:
        multi = num * num2
        print(f'Sua operação escolhida foi multiplicação. Esse é o resultado: {multi}')
    elif calcular == 4:
        print(f'Sua operação escolhida foi divisão. Esse é o resultado: {num/num2}')
    elif calcular == 5:
        break



