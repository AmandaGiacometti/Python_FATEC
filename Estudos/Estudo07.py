tamanho = float(input("Informe o tamanho do arquivo em MiB "))
velo = float(input("Informe a velocidade da sua internet em Mbps "))

bits = tamanho * 8
tempoS = bits / velo
tempoM = tempoS / 60

print ("\nTamanho do arquivo :{:>8.0f} MiB".format(tamanho))
print ("Velocidade         :{:>8.0f} Mbps".format(velo))
print ("Tempo do download  :{:>8.0f} minutos(s)".format(tempoM))

a = input("\nDigite enter para sair")
