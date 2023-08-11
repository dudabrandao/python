num1 = []
while True:
    num1.append(int(input("Digite um número: ")))
    res = str(input("Deseja continuar? (S/N)"))
    if res in "Nn":
        break
num1.sort()
print(f"Os números são{num1}")
