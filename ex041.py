#Faça um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade

from datetime import date
atual = date.today().year
nasc = int(input("Digite o seu ano de nascimento: "))
idade = atual - nasc
print("O atleta tem {} anos.".format(idade))
if idade <= 9:
    print("Classificação MIRIM!")
elif idade <= 14:
    print("Classificação INFANTIL!")
elif idade <= 19:
    print("Classificação JUNIOR!")
elif idade <= 25:
    print("Classificação SÊNIOR!")
else:
    print("Classificação MASTER!")