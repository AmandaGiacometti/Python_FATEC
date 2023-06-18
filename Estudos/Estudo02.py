num = int(input("Digite num para calcular fatorial"))
fat = 1
ini = num
while num > 0 :
    fat = fat * num
    num = num - 1
print(" %2d! = %d" %(ini, fat))

# Outra solução:

num = int(input("Digite um numero para calculo do fatorial: "))
fat = 1
ini = num

while num > 1:
    fat = fat * num
    num = num - 1

print("O fatorial de {} = {}".format(ini, fat))
a = input("Digite enter para sair.")