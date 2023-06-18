print("Programa para verificação de data")

dia=mes=ano=erro=0
dd= [00,31,28,31,30,31,30,31,31,30,31,30,31]

digita = "s"

while digita == "s":
	dia=input("Digite o dia: ")
	mes=input("Digite o mes: ")
	ano=input("Digite o ano: ")

	if dia.isdigit():
		dia = int(dia)
	else:
		dia=0
		erro=1

	if mes.isdigit():
		mes = int(mes)
	else:
		mes=0
		erro=1

	if ano.isdigit():
		ano = int(ano)
	else:
		ano=0
		erro=1

	if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
		dd[2] = 29

	if mes < 1 or mes > 12:
		erro=1
	else:
		if dia < 1 or dia > dd[mes]:
			erro=1
	if ano < 1:
		erro=1

	digita = "?"

	if erro == 1:
		while digita != "s" and digita != "n":
			digita= input("Data incorreta, deseja corrigir? s ou n ")
		if digita == "n":
			print("Digitação abandonada")
		erro = 0
	else:
		print("Data digitada válida")

a = input("Digite enter para sair")