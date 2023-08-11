soma = 0
qnt = 0
while True:
    ini = float(input("Digite número: "))
    qnt += 1
    soma += ini
    if ini < 0:
        media = soma / qnt
        print(f"A média é de {media}")
        break
    f = str(input("Deseja continuar? [S/N]: "))
    if f.lower() == "n":
        media= soma / qnt
        print(f"A média é de {media}")
        break
