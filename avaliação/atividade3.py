nome = str(input("Digite seu nome: "))#nome da pessoa
salariofixo = float(input("Digite seu salário fixo: "))#salario fixo da pessoa
totaldevendas = float(input("Digite o total de vendas efetuadas no mês: "))#total de vendas

porcentagem = (totaldevendas / 100) * 15 #operação pra saber quanto vale 15% do total de vendas
salariototal = porcentagem + salariofixo# soma dos 15% + o salário fixo

print(salariototal)#salario total com os 15%