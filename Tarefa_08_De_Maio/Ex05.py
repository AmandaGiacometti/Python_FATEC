# Dadas quatro medidas, informar se as mesmas formam um quadrado, um retângulo ou se não formam nenhuma das figuras
# anteriores.

A = int(input("Digite o primeiro número: "))
B = int(input("Digite o segundo número: "))
C = int(input("Digite o terceiro número: "))
D = int(input("Digite o quarto número: "))

if A == B and B == C and C == D:
    print("Estes valores formam um quadrado.")
elif (A == B and C == D) or (A == C and B == D) or (A == D and B == C):
    print("Estes valores formam um retângulo.")
else:
    print("Estes valores não formam nem um quadrado nem um retângulo.")

