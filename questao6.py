#Questão6

salario = float(input("Digite o salário do colaborador: "))

if salario <= 280:
    percentual = 20
elif salario <= 700:
    percentual = 15
elif salario <= 1500:
    percentual = 10
else:
    percentual = 5

aumento = (percentual/100) * salario
novo_salario = salario + aumento

print("Salário antes do reajuste: R$ {:.2f}".format(salario))
print("Percentual de aumento aplicado: {}%".format(percentual))
print("Valor do aumento: R$ {:.2f}".format(aumento))
print("Novo salário, após o aumento: R$ {:.2f}".format(novo_salario))