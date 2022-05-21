#Crie um programa que leia o ano de nascimenyo de 7 pessoas e mostre quantas pessoas são maiores de idade e quantas são menores

from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1,8):
    ano = int(input("Em que ano a {}ª pessoa nasceu? ".format(c)))
    idade = atual - ano
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print("Há {} pessoas maiores de idade!".format(totmaior))
print("Há {} pessoas menores de idade!".format(totmenor))

