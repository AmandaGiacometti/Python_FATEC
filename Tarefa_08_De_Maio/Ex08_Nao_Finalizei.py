# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre seu
# salário bruto (valor hora * número de horas), os descontos e o salário líquido no referido mês, sabendo-se que são
# descontados: INSS de acordo com a tabela anexa, o Imposto de Renda Retido na Fonte (IRRF) de acordo com a tabela
# anexa e 5% para o sindicato sobre o salário bruto.

# # # NÃO ESTÁ FINALIZADO # # #

renda = float(input("Digite quanto você ganha por hora: "))
horas = int(input("Digite o número de horas trabalhadas por mês: "))

bruto = renda * horas
sind = 0.05 * bruto

if bruto <= 1045.0:
    inss = 0.925 * bruto
    print("Salário Bruto: R$ ",bruto,"// INSS: R$ ",0.075 * bruto,"// IRRF: R$ ",,"// Sindicato: R$ ",sind,"// Salário Liquido: R$ ",)

elif 1045.0 < bruto <= 1903.99:
    inss = 0.91 * bruto
    print("Salário Bruto: R$ ", bruto,"// INSS: R$ ",0.09 * bruto, "// IRRF: R$ ",, "// Sindicato: R$ ", sind, "// Salário Liquido: R$ ",)

elif 1903.99 < bruto <= 2089.6:
    inss = 0.91 * bruto
    print("Salário Bruto: R$ ", bruto,"// INSS: R$ ",0.09 * bruto, "// IRRF: R$ ",, "// Sindicato: R$ ", sind, "// Salário Liquido: R$ ",)

elif 2089.6 < bruto <= 2826.65:
    inss = 0.88 * bruto
    print("Salário Bruto: R$ ", bruto,"// INSS: R$ ",0.12 * bruto, "// IRRF: R$ ",, "// Sindicato: R$ ", sind, "// Salário Liquido: R$ ",)

elif 2826.65 < bruto <= 3134.4:
    inss = 0.88 * bruto
    print("Salário Bruto: R$ ", bruto,"// INSS: R$ ",0.12 * bruto, "// IRRF: R$ ",, "// Sindicato: R$ ", sind, "// Salário Liquido: R$ ",)

elif 3134.4 < bruto <= 3751.05:
    inss = 0.86 * bruto
    print("Salário Bruto: R$ ", bruto,"// INSS: R$ ",0.14 * bruto, "// IRRF: R$ ",, "// Sindicato: R$ ", sind, "// Salário Liquido: R$ ",)

elif 3751.05 < bruto <= 4664.68:
    inss = 0.86 * bruto
    print("Salário Bruto: R$ ", bruto,"// INSS: R$ ",0.14 * bruto, "// IRRF: R$ ",, "// Sindicato: R$ ", sind, "// Salário Liquido: R$ ",)

elif 4664.68 < bruto <= 6101.06:
    inss = 0.86 * bruto
    print("Salário Bruto: R$ ", bruto,"// INSS: R$ ",0.14 * bruto, "// IRRF: R$ ",, "// Sindicato: R$ ", sind, "// Salário Liquido: R$ ",)

else:
    print("Valores não constam na base")