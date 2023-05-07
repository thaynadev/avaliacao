#Questão8

notas = []
valor = 0

while valor != -1:
    valor = float(input("Digite uma nota ou -1 para encerrar: "))
    if valor != -1:
        notas.append(valor)

quantidade = len(notas)
soma = sum(notas)
media = soma / quantidade
acima_da_media = sum(1 for nota in notas if nota > media)
abaixo_de_sete = sum(1 for nota in notas if nota < 7)

print(f"Foram lidos {quantidade} valores: {notas}")
print(f"Valores na ordem inversa: ")
for nota in reversed(notas):
    print(nota)

print(f"Soma das notas: {soma}")
print(f"Média das notas: {media:.2f}")
print(f"Notas acima da média: {acima_da_media}")
print(f"Notas abaixo de 7: {abaixo_de_sete}")

print("Programa encerrado.")