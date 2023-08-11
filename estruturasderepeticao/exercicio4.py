qnum = 0
for n in range(1, 101):
    if n % 7 == 0 and n % 5 != 0:
        qnum += 1
        print(n)
print('Quantidade de números: ',qnum)
