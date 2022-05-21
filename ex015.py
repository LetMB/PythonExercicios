#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado

km = float(input("Digite quantos km o carro rodou: "))
dias = int(input("Digite por quantos dias o caro foi alugado: "))
valor = (km*0.15)+(dias*60)
print("O preço a pagar por {}km rodados e {} dias de aluguel foi de {:.2f}R$".format(km,dias,valor))