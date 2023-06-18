# Elabore um algoritmo que leia um ano pelo teclado e informe se o mesmo é bissexto ou não.
# Lembrando que um ano é bissexto se for divisível por 4 e não por 100, ou se for divisível por 400.

ano = int(input("Digite um ano e descubra se ele é bissexto: "))

if ano <= 0:
    print("Ano inválido!")
elif ano % 400 == 0:
    print("O ano é bissexto!")
elif ano % 4 == 0 and ano % 100 != 0:
    print("O ano é bissexto!")
else:
    print("O ano NÃO é bissexto!")

# Resolução mais enxuta:

ano = int(input("Digite um ano e descubra se ele é bissexto: "))

if ano <= 0:
    print("Ano inválido!")
elif (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano é bissexto!")
else:
    print("O ano NÃO é bissexto!")
