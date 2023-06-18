print("Vetor de 10 elementos de forma crescente")
vet = [0]*10
aux = 0
for x in range(0, 10):
    vet[x] = int(input("Digite um número: "))

for a in range(0, 9):
    for b in range(a+1, 10):
        if vet[a] > vet[b]:
            aux = vet[a]
            vet[a] = vet[b]
            vet[b] = aux

print("Os números em ordem crescente são: ",end="")

for x in range (0, 10):
    print(vet[x]," ", end="")

a = input("\nDigite enter para sair")