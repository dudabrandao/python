qtpessoas=int(input("Digite a quantidade de pessoas: "))
soma_idades_mulheres = 0
soma_idades_homens = 0
soma_idades_grupo = 0
contador_mulheres = 0
contador_homens = 0

for n in range (1,qtpessoas+1):
    pessoa = str(input("Digite seu nome aqui: "))
    idade = int(input("Digite a idade da pessoa : "))
    sexo = input("Digite o sexo da pessoa (M/F): ")
    if sexo.lower() == "f":
        soma_idades_mulheres += idade
        contador_mulheres += 1
    elif sexo.lower() == "m":
        soma_idades_homens += idade
        contador_homens += 1
    else:
        print("Sexo inválido! Digite 'M' para masculino ou 'F' para feminino.")

    soma_idades_grupo += idade

media_mulheres = soma_idades_mulheres / contador_mulheres
media_homens = soma_idades_homens / contador_homens
media_grupo = soma_idades_grupo / qtpessoas

print(f"A média das idades geral é {media_grupo}")
print(f"A média das mulheres é {media_mulheres}")
print(f"A média dos homens é {media_homens}")

