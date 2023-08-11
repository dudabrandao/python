fruta = ["melancia", "banana", "abacaxi", "uva"]
fruta[3] = "melancia" #as listas são mutáveis

print(fruta)

#----------adicionar itens na lista--------------------

fruta = ["melancia", "banana", "abacaxi", "uva"]
fruta.append("laranja")

print(fruta)

# parenteses - tupla and colchetes - lista

#---------criar elmentos no inicio da lista---------------

fruta = ["melancia", "banana", "abacaxi", "uva", "laranja"]
fruta.insert(0,"morango")

print(fruta)

#---------criar elmentos na posição 1---------------

fruta = ["melancia", "banana", "abacaxi", "uva", "laranja"]
fruta.insert(1,"morango")

#--------lista números---------------------------

num = [7,5,3,0,9,6]
num.sort()#ordem crescente
num.sort(reverse = True)#ordem decrescente

#obs: funciona com strings

#-------------Soma de todos os números da lista

num = [7,5,3,0,9,6]
soma = sum (num)
print(f"O resultado da soma é: {soma}")

#----------maior e o menor num da lista

num = [7,5,3,0,9,6]
maior=max(num)
menor=min(num)
print(f"O maior e o menor número dessa lista é respectivamente: {maior} e {menor}")

#----------qual a palavra com maior caracteres-----------

fruta = ["melancia", "banana", "abacaxi", "uva", "laranja"]
maior=max(fruta,key=len)
menor=min(fruta,key=len)
print(f"Maior: {maior}")
print(f"Menor: {menor}")

#-------------------cópia da lista 1-----------------------

num1 = [7,5,3,0,9,6]
num2 = num1[:]
num2[1] = 2

print(f"Lista 1: {num1}")
print(f"Lista 2: {num2}")

#------------------------------------------------------------

num1 = []
while True:
    num1.append(int(input("Digite um número: ")))
    res = str(input("Deseja continuar? (S/N)"))
    if res in "Nn":
        break
    print(f"Os números são{num1}")

#-----------------------------------------------------------

lista = [1, 2, 3, 4, 5]

lista = [1, 2, 3, 4, 5]
print(lista[0]) # Saída: 1
print(lista[2]) # Saída: 3
print(lista[-1]) # Saída: 5 (último elemento)

lista = [1, 2, 3, 4, 5]
lista.append(6) # Adiciona o número 6 ao final da lista
lista.insert(0, 0) # Insere o número 0 no início da lista
lista.remove(3) # Remove o número 3 da lista
elemento = lista.pop() # Remove e retorna o último elemento da lista


lista = [1, 2, 3, 4, 5]
for elemento in lista:
  print(elemento)

