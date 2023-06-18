# Elabore um algoritmo que leia três números pelo teclado, coloque-os em ordem crescente (N<=N2<=N3) e mostre-os
# em ordem crescente no monitor.

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
num3 = input("Digite o terceiro número: ")

if num1 <= num2 and num2 <= num3:
    print("Em ordem crescente: ",num1,", ",num2,", ",num3)
elif num1 <= num3 and num3 <= num2:
    print("Em ordem crescente: ",num1,", ",num3,", ",num2)
elif num2 <= num1 and num1 <= num3:
    print("Em ordem crescente: ",num2,", ",num1,", ",num3)
elif num2 <= num3 and num3 <= num1:
    print("Em ordem crescente: ",num2,", ",num3,", ",num1)
elif num3 <= num1 and num1 <= num2:
    print("Em ordem crescente: ",num3,", ",num1,", ",num2)
else:
    print("Em ordem crescente: ", num3, ", ", num2, ", ", num1)