qtpessoas=int(input("Digite a quantidade de pessoas: "))
homemmaisvelho = 0
mulheresmenos20 = 0
idadevelho = 0

for n in range (1,qtpessoas+1):
    pessoa = str(input("Digite seu nome aqui: "))
    idade = int(input("Digite a idade da pessoa : "))
    sexo = input("Digite o sexo da pessoa (M/F): ")
    if idade < 20 and sexo == "f":
        mulheresmenos20 =+ 1
    if sexo.lower() == "m" and idade > idadevelho:
        idadevelho = idade
        nomevelho = homemmaisvelho

print(f"Número de mulheres com idade menor que 20: {mulheresmenos20} ")