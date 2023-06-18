n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))
aux = float

if n1 > n2 :
	aux = n1
	n1 = n2
	n2 = aux

if n1 > n3 :
	aux = n1
	n1 = n3
	n3 = aux

if n1 > n4 :
	aux = n1
	n1 = n4
	n4 = aux

if n2 > n3 :
	aux = n2
	n2 = n3
	n3 = aux

if n2 > n4 :
	aux = n2
	n2 = n4
	n4 = aux

if n3 > n4 :
	aux = n3
	n3 = n4
	n4 = aux

print("\nNúmeros digitados em ordem crescente: ", n1, n2, n3, n4)

a = input("\nPressione enter para sair")