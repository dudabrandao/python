while True:
    num = int(input('Digite um número: '))
    if num < 0:
        print('Número inválido')
        break
    elif num == 999:
        print('Número muito grande')
        break