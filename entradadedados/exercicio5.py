valor= float(input("Digite aqui o valor: "))
taxa= int(input("Digite aqui o valor da taxa: "))
tempo= int(input("Digite aqui o tempo: "))

prestacao= valor + (valor* (taxa/100)* tempo)

print(f"O valor da prestação em atraso é de {prestacao} reais")


