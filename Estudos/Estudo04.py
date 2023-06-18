print("Combinação de 6 num de 4 em 4")
vet = [0] * 6
for x in range (0, 6):
    vet[x] = input("Digite um número: ")

for a in range (0, 3):
    for b in range (a+1, 4):
        for c in range (b+1, 5):
            for d in range (c+1, 6):
                print(vet[a]," ",vet[b]," ",vet[c]," ",vet[d])

e = input("Digite enter para sair")