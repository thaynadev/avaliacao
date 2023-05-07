# lista de contadores para armazenar a quantidade de vendedores em cada intervalo de salário
contadores = [0] * 10

# loop para receber as vendas brutas dos vendedores e calcular seus salários
while True:
    vendas = float(input("Informe as vendas brutas (ou -1 para encerrar): "))
    if vendas == -1:
        break
    salario = 200 + vendas * 0.09
    posicao = int((salario - 200) // 100)  # fórmula para determinar a posição do intervalo
    if posicao < 0:  # tratamento para salários menores que $200
        posicao = 0
    elif posicao > 9:  # tratamento para salários maiores que $1000
        posicao = 9
    contadores[posicao] += 1

# exibição dos resultados
for i in range(len(contadores)):
    if i == 0:
        print("$200 - $299:", contadores[i])
    elif i == 9:
        print("$1000 em diante:", contadores[i])
    else:
        print(f"${200 + i*100} - ${299 + i*100}:", contadores[i])