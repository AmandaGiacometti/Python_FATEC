num = int(input("Digite um numero maior que 9 "))

ult = 0

ult = num % 10

while num > 9 :
	num = num // 10

if num == ult :
	print("Primeiro e ultimo digitos sao iguais! {} e {}".format(num,ult))
else:
	print("Primeiro e ultimo digitos sao diferentes!",num," e ",ult)
a = input("\nDigite enter para sair")