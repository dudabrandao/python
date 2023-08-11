pessoa = ["Duda", 16, 1.50]
print(pessoa[0])

# declarando uma biblioteca

pessoa = {"Nome":"Duda", "Idade": 16, "Altura": 1.50}
print(pessoa["Nome"])
pessoas = {}
pessoas1 = dict()

#------------------FATIAMENTO------------------

pessoa = {"Nome":"Duda", "Idade": 16, "Altura": 1.50}
pessoa["Peso"] = 60.5 # adicionar
del pessoa["Peso"] # deletar
print(pessoa)

pessoa = {"Nome":"Duda", "Idade": 16, "Altura": 1.50}
pessoa2 = {"Nome":"Brenda", "Idade": 16, "Altura": 1.50, "Sexo": "F"}
pessoa.update(pessoa2)
pessoa2["Idade"] = 15
print(pessoa)
print(pessoa2)

#-------------------------------------------------------

pessoa = {"Nome":"Duda", "Idade": 16, "Altura": 1.50}
print(pessoa.values())#valores
print(pessoa.keys())#chaves
print(pessoa.items())#chaves e valores

#------------------------------------------------------

for K in pessoa.keys():
    print(K)#imprimi as chaves uma embaixo da outra

for V in pessoa.values():
    print(V)#imprimi os valores um embaixo do outro

for K,V in pessoa.items():
    print(f"O item {K} é {V}")

#--------------------------------------------------------

pessoa = {"Nome":"Duda", "Idade": 16, "Altura": 1.50}
idaded = int(input("Digite sua idade: "))
if idaded in pessoa.values():
    print("Você tem a mesma idade que a Duda")

dicionario = {"nome": "João", "idade": 25, "cidade": "São Paulo"}

dicionario = {"nome": "João", "idade": 25, "cidade": "São Paulo"}
print(dicionario["nome"]) # Saída: João
print(dicionario["idade"]) # Saída: 25

dicionario = {"nome": "João", "idade": 25, "cidade": "São Paulo"}
dicionario["profissão"] = "Engenheiro" # Adiciona uma nova chave-valor ao dicionário
dicionario.pop("idade") # Remove a chave-valor correspondente à chave "idade"
chaves = dicionario.keys() # Retorna uma lista com as chaves do dicionário
valores = dicionario.values() # Retorna uma lista com os valores do dicionário

pythonCopy code
dicionario = {"nome": "João", "idade": 25, "cidade": "São Paulo"}
for chave, valor in dicionario.items():
  print(chave, ":", valor)

