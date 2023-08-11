# Aluna: Maria Eduarda Ferreira Brandão - Questão: "Bazinga!"

print("Escolham entre Pedra, Papel, Tesoura, Lagarto, Spock.")#coloquei as opções de escolha do jogador
jog1= str(input("Jogador 1(Sheldon): "))#jogador1
jog2= str(input("Jogador 2(Raj): "))#jogador2

#defini todas as possibilidades possíveis para o jogo, quando o sheldon ganhasse coloquei a mensagem adequada, assim com as seguintes possibilidades.
if jog1 == "pedra" and jog2 == "papel":
    print("BAZINGA! Sheldon venceu!")
elif jog1 == "papel" and jog2 == "pedra":
    print("BAZINGA! Sheldon venceu!")
elif jog1 == "pedra" and jog2 == "lagarto":
    print("BAZINGA! Sheldon venceu!")
elif jog1 == "lagarto" and jog2 == "spock":
    print("BAZINGA! Sheldon venceu!")
elif jog1 == "spock" and jog2 == "tesoura":
    print("BAZINGA! Sheldon venceu!")
elif jog1 == "tesoura" and jog2 == "lagarto":
    print("BAZINGA! Sheldon venceu!")
elif jog1 == "lagarto" and jog2 == "papel":
    print("BAZINGA! Sheldon venceu!")
elif jog1 == "papel" and jog2 == "spock":
    print("BAZINGA! Sheldon venceu!")
elif jog1 == "spock" and jog2 == "pedra":
    print("BAZINGA! Sheldon venceu!")
elif jog1 == "pedra" and jog2 == "tesoura":
    print("BAZINGA! Sheldon venceu!")
elif jog1 == "papel" and jog2 == "tesoura":
    print("Raj trapaceou!")
elif jog1 == "pedra" and jog2 == "papel":
    print("Raj trapaceou!")
elif jog1 == "lagarto" and jog2 == "pedra":
    print("Raj trapaceou!")
elif jog1 == "spock" and jog2 == "lagarto":
    print("Raj trapaceou!")
elif jog1 == "tesoura" and jog2 == "spock":
    print("Raj trapaceou!")
elif jog1 == "lagarto" and jog2 == "tesoura":
    print("Raj trapaceou!")
elif jog1 == "papel" and jog2 == "lagarto":
    print("Raj trapaceou!")
elif jog1 == "spock" and jog2 == "papel":
    print("Raj trapaceou!")
elif jog1 == "pedra" and jog2 == "spock":
    print("Raj trapaceou!")
elif jog1 == "tesoura" and jog2 == "pedra":
    print("Raj trapaceou!")
elif jog1 == "papel" and jog2 == "papel":
    print("EMPATE! De novo!")
elif jog1 == "pedra" and jog2 == "pedra":
    print("EMPATE! De novo!")
elif jog1 == "tesoura" and jog2 == "tesoura":
    print("EMPATE! De novo!")
elif jog1 == "lagarto" and jog2 == "lagarto":
    print("EMPATE! De novo!")
elif jog1 == "spock" and jog2 == "spock":
    print("EMPATE! De novo!")