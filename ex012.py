#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

p = float(input("Qual o preço do produto? R$"))
d = p * 0.95
print("O produto de {:.2f} reais, com desconto de 5%, fica por {:.2f} reais.".format(p,d))