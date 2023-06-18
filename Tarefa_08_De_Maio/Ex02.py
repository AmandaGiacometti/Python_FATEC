# Elabore um algoritmo que leia um numero pelo teclado e informe no monitor de vídeo se o número é par ou ímpar.

num = int(input("Digite um número e descubra se ele é par ou ímpar: "))

if num % 2 == 0:
    print("O número digitado é par.")
else:
    print("O número digitado é ímpar.")
