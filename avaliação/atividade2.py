while True:#looping
    nota1 = float(input("Digite uma nota: ")) #pergunta nota 1

    while nota1 < 0 or nota1 > 10:#validando a nota1
        print("Nota inválida!")
        nota1 = float(input("Digite uma nota: "))#caso a nota seja inválida pergunta novamente a nota

    nota2 = float(input("Digite uma nota: "))#pergunta nota 2

    while nota2 < 0 or nota2 > 10:#validando a nota 2
        print("Nota inválida!")
        nota2 = float(input("Digite uma nota: "))#caso a nota seja inválida pergunta novamente a nota

    media = (nota1 + nota2) / 2 #operação da média
    print(f"Sua média é: {media}")#aparecer a média

    simounao = 0

    while simounao != 1 and simounao != 2:# calculo novo
        resposta = int(input("Novo cálculo? (1-Sim/2-Não)")) #pergunta pra novo cálculo ou não
        if resposta == 1: #se a resposta for não parar aqui
            break