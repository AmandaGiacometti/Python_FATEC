# Informados três valores (A, B e C), verificar se os mesmos podem ser os comprimentos dos
# lados de um triângulo e, se forem, verificar se formam um triângulo equilátero, isósceles ou escaleno.
# Informar se não compuserem nenhum triângulo.

A = int(input("Digite o primeiro número: "))
B = int(input("Digite o segundo número: "))
C = int(input("Digite o terceiro número: "))

if ((A <= B and B <= C) and (A + B) <= C) or ((A <= C and C <= B) and (A + C) <= B) or ((B <= A and A <= C) and (B + A) <= C) or ((B <= C and C <= A) and (B + C) <= A) or ((C <= A and A <= B) and (C + A) <= B) or ((C <= B and B <= A) and (C + B) <= A):
		print("Não forma um triângulo!")

elif A == B and B == C:
	print("Forma um triângulo equilátero")

else:
	if (A == B) or (A == C) or (B == C):
		print("Forma um triângulo isóceles")

	else:
		print("Forma um triângulo escaleno")