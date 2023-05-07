#Questão3

# pedindo a altura da pessoa
altura = float(input("Digite sua altura em metros: "))

# calculando o peso ideal para homens e mulheres
peso_ideal_homem = (72.7 * altura) - 58
peso_ideal_mulher = (62.1 * altura) - 44.7

# exibindo o resultado na tela
print("Para um homem com", altura, "m de altura, o peso ideal é:", peso_ideal_homem, "kg")
print("Para uma mulher com", altura, "m de altura, o peso ideal é:", peso_ideal_mulher, "kg")