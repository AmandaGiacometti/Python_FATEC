print("maior e menor valor digitado - 9999 encerra")

maior=num=0
menor=10000

num = int(input("Digite um número entre 1 e 1000"))
while num != 9999 :
    if num < menor : menor = num
    if num > maior : maior = num
    num = int(input("Digite um número entre 1 e 1000"))
if menor == 10000 : print("sem digitação")
else:
    print("O menor número digitado é: ",menor)
    print("O maior número digitado é: ",maior)

################### Outra maneira:

print ("Digite diversos numeros ente 0 e 1000. Digite 9999 para encerrar")

num=maior=0
menor=10000

while num != 9999:
	num = int(input("Digite um numero de 0 a 1000: "))
	if num == 9999: break
	if num < menor:
		menor = num
	if num > maior:
		maior = num

if menor == 10000:
	print("Sem digitação")
else:
	print("O menor número digitado foi {}".format(menor))
	print("O maior número digitado foi {}".format(maior))

a = input("Digite enter para sair")

################ Terceira maneira:

print ("Digite diversos numeros ente 0 e 1000. Digite 9999 para encerrar")

num = int(input("Digite o primeiro numero: "))
if num == 9999:
	exit()
num2 = int(input("Digite o segundo numero: "))
if num2 == 9999:
	exit()

menor = 0
maior = 0

if num < num2:
	menor = num
	maior = num2
else:
	menor = num2
	maior = num

while num != 9999 :
	num = int(input("Digite outro numero :"))
	if num == 9999 : break
	if num < menor :
		menor = num
	if num > maior :
		maior = num
print ("Numero menor = ",menor," o numero maior = ",maior)
a = input("Digite enter para sair")

