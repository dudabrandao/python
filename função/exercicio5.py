def ficha(nome, gols):
    print(f'o jogador {nome} marcou {gols} gols')

nomejogador = input('digite o nome do jogador: ')
golsmarcados = int(input('digite a quantidade de gols marcados: '))
ficha(nomejogador, golsmarcados)