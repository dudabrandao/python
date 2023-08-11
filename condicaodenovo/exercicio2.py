valordacompra= float(input("Digite o valor total da compra: "))
numerodeprestacao= int(input("Digite em quantos meses a compra foi parcelada: "))

valordaparcela= valordacompra/numerodeprestacao

if valordaparcela > 500.00:
    print("Você não irá conseguir pagar as parcelas!")
else:
    print(f"O valor da parcela é: {valordaparcela}")


