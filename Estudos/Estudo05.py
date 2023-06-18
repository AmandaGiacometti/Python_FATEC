print('Combinação de 10 numeros, 7 a 7')
vet=[0]*10
cont = 0
for x in range (0,10):
	vet[x]=input('Digite um número: ')
for a in range(0,4):
	for b in range(a+1,5):
		for c in range(b+1,6):
			for d in range(c+1,7):
				for e in range(d+1,8):
					for f in range(e+1,9):
						for g in range(f+1,10):
							print(vet[a]," ",vet[b]," ",vet[c]," ",vet[d]," ",vet[e]," ",vet[f]," ",vet[g])
							cont = cont + 1
print(cont)