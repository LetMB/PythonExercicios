#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import date

def voto(ano):
    idade = date.today().year - ano
    if idade >= 18:
        print(f"Com {idade} anos o VOTO É OBRIGATÓRIO!")
    elif idade < 16:
        print(f"Com {idade} anos o VOTO É PROIBIDO!")
    else:
        print(f"Com {idade} anos o VOTO É OPCIONAL!")

nasc = int(input("Ano de nascimento: "))
print(voto(nasc))