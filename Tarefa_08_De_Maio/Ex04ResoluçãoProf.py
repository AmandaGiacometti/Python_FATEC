# Informados três valores (A, B e C), verificar se os mesmos podem ser os comprimentos dos
# lados de um triângulo e, se forem, verificar se formam um triângulo equilátero, isósceles ou escaleno.
# Informar se não compuserem nenhum triângulo.

# RESOLUÇAÕ DO PROFESSO ARNALDO:

A = int(input("Digite o primeiro número: "))
B = int(input("Digite o segundo número: "))
C = int(input("Digite o terceiro número: "))

if A <= (B + C) and B <= (A + C) and C <= (A + B):

	if A == B and B == C:
		print("Forma um triângulo equilátero")

	elif A == B or B == C or A == C:
		print("Forma um triângulo isóceles")

	else:
		print("Forma um triângulo escaleno")

else:
	print("Não forma um triângulo")