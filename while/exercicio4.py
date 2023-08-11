vcaro = 0
ncaro = ''
total = 0
while True:
    produto = input('Qual o produto que deseja comprar: ')
    valor = float(input('Qual o valor desse produto: '))
    if valor > vcaro:
        vcaro = valor
        ncaro = produto
        total += valor
        continua = input('Deseja continuar? [s/n]: ')
        if continua != 's':
            break
print(f'O total de sua compra foi: {total}')
print(f'O produto mais caro foi: {ncaro}')