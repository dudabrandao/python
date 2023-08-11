numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

opcoes = int(input('Digite o número desejado para realizar a respectiva operação\n(1-adição/2-subtração/3-multiplicação/4-divisão): '))

if opcoes == 1:
    print('o resultado da adição é: ', numero1 + numero2)
elif opcoes == 2:
    print('o resultado da subtração é: ', numero1 - numero2)
elif opcoes == 3:
    print('o resultado da multiplicação é: ', numero1 * numero2)
elif opcoes == 4:
    print('o resultado da divisão é: ', numero1 % numero2)