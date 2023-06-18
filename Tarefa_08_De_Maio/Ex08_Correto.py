salarioHora = float(input("Informe o seu salário por hora: "))
hora = int(input("Informe o número de horas trabalhadas no mês: "))

bruto = salarioHora * hora
inss = bruto * 0.11
irpf = bruto * 0.27
sind = bruto * 0.05
liq = bruto - (inss + irpf + sind)

print ("\n+ Salário Bruto:   R$ {:>10,.2f}".format(bruto))
print ("- INSS (11%):      R$ {:>10,.2f}".format(inss))
print ("- IRPF (27%):      R$ {:>10,.2f}".format(irpf))
print ("- Sindicato (5%):  R$ {:>10,.2f}".format(sind))
print ("= Salário Líquido: R$ {:>10,.2f}".format(liq))

a = input("\nPressione enter para sair")



