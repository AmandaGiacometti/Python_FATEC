# Elabore um algoritmo que leia uma data desmembrada em dia, mês e ano e um valor com a quantidade de dias, entre
# 1 e 20, para projetar a data lida em uma data futura válida. Não é necessário validar os dados de entrada (data
# lida e quantidade de dias).

dia = int(input("Digite um dia: "))
mes = int(input("Digite um mes: "))
ano = int(input("Digite um ano: "))
fut = int(input("Digite quantos dias você quer adicionar à data (máximo 20): "))

if dia <= 0 or fut <= 0 or fut > 20:
    print("Valor(res) inválido(s)")

elif (mes == 2):
    if (dia + fut) <= 28:
        print("A nova data é: ",dia + fut,"/",mes,"/",ano)
    else:
        print("A nova data é: ",(dia + fut) - 28,"/",mes + 1,"/",ano)

elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10):
    if (dia + fut) <= 31:
        print("A nova data é: ",dia + fut,"/",mes,"/",ano)
    else:
        print("A nova data é: ",(dia + fut) - 31,"/",mes + 1,"/",ano)

elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    if (dia + fut) <= 30:
        print("A nova data é: ",dia + fut,"/",mes,"/",ano)
    else:
        print("A nova data é: ",(dia + fut) - 30,"/",mes + 1,"/",ano)

elif mes == 12:
    if (dia + fut) <= 30:
        print("A nova data é: ",dia + fut,"/",mes,"/",ano)
    else:
        print("A nova data é: ",(dia + fut) - 31,"/ 1 /",ano + 1)

else:
    print("Valor(res) inválido(s)")