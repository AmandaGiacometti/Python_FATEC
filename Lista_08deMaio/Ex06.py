# Elabore um algoritmo que leia uma data desmembrada em dia, mês e ano, verifique se a data digitada é uma data válida
# ou não e emita uma única mensagem: “data válida” ou “data inválida”.

dia = int(input("Digite um dia: "))
mes = int(input("Digite um mes: "))
ano = int(input("Digite um ano: "))

if mes <= 0 or mes > 12 or dia <= 0 or ano <= 1500 or ano > 2200:
    print("A data digitada é INVÁLIDA")

elif (mes == 2) and (dia > 28):
    print("A data digitada é INVÁLIDA")

elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and (dia > 31):
    print("A data digitada é INVÁLIDA")

elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and (dia > 30):
    print("A data digitada é INVÁLIDA")

else:
    print("A data digitada é válida! ",dia,"/",mes,"/",ano)