#while 30<20:
    #print("Olá, Mundo!")
#while 10<20:
    #print("Olá, Mundo!")

#-----------------------------#
#num=0
#while num<20:
#    print(num)
#    num+=1

#-----------------------------#
#Res= "S"
#while Res == "S":
    #num= int(input("Digite: "))
    #Res= str(input("Deseja continuar? (S/N)"))

# _----------------------------------------#

Res= "S"
while Res == "S":
    num= int(input("Digite: "))
    if num == 999:
        print("Número muito grande.")
        break
    Res = str(input("Deseja continuar? (S/N)"))