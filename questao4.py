#Questão4

valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas
ir = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos

print("Salário Bruto: R$ {:.2f}".format(salario_bruto))
print("Descontos:")
print(" - IR (11%): R$ {:.2f}".format(ir))
print(" - INSS (8%): R$ {:.2f}".format(inss))
print(" - Sindicato (5%): R$ {:.2f}".format(sindicato))
print("Total de descontos: R$ {:.2f}".format(descontos))
print("Salário Líquido: R$ {:.2f}".format(salario_liquido))
