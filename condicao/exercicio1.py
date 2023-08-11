Prova1=int(input("Digite aqui a primeira nota: "))
Prova2=int(input("Digite aqui a segunda nota: "))

media= (Prova1 + Prova2)/2

if media < 6:
    print(f"Você reprovou! Sua média é: {media} ")
else media >= 6:
    print(f"Você está aprovado! Sua média é: {media}")

