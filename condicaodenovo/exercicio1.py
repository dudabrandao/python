var1= int(input("Digite quantos gols foram feitos pelo time1: "))
var2= int(input("Digite quantos gols foram feitos pelo time2: "))

if var1 == var2:
    print(f"O resultado do jogo foi empate: {var1} X {var2}")
elif var1 < var2:
    print(f"O resultado do jogo foi vitória do time 2: {var1} X {var2}")
else:
    print(f"O resultado do jogo foi vitória do time 1: {var1} X {var2}")