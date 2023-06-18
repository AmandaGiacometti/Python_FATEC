L1 = int(input('Informe o comprimento de um lado '))
L2 = int(input('Informe o comprimento do outro lado '))
area = int(L1 * L2)
custoLitro = float(14.00)
custoTotal = area / 2 * custoLitro

print ("\nA metragem da área é                 = {:>7} m2".format(area))
print ("A quantidade de litros necessária é  = {:>10,.2f}".format(area/2))
print ("O custo total da pintura é           = {:>10,.2f}".format(custoTotal))

a = input("\nPressione enter para sair")