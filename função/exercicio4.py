def voto(nascimento):
    idade = 2023 - nascimento

    if idade < 16:
        return 'voto negado'
    elif 16 <= idade < 18 or idade >= 70:
        return 'voto opcional'
    else:
        return 'voto obrigatório'

ano = int(input('digite o ano de nascimento: '))
result = voto(ano)
print(result)