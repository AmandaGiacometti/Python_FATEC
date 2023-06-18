print("Programa para cálculo de combinações de números.\n")

def fatorial (num):
	"Função para cálculo de fatorial"
	fat = 1
	while num > 1:
		fat = fat * num
		num = num - 1
	return fat

n = int(input("Informe a quantidade de números a combinar: "))
k = int(input("Informe o número de agrupamento desejado: "))

comb = int(fatorial(n) / (fatorial(k) * fatorial(n-k)))

print("\nA quantidade de combinações possíveis para {} números combinados {} a {} é: {:,}.".format(n,k,k,comb))

a = input("\nDigite enter para sair.")