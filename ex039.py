#Faça um programa que leia o ano de nascimenyo de um jovem e informe se ele ainda deve se alistar no serviço militar, se é hora de se alistar ou se já passou o tempo do alistamento

from datetime import date

atual = date.today().year
nasc = int(input("Ano de nascimento: "))
idade = atual - nasc
if idade == 18:
    print("Quem nasceu em {} tem {} anos em {} e deve se alistar imediatamente!".format(nasc, idade, atual))
elif idade < 18:
    saldo = 18 - idade
    print("Quem nasceu em {} tem {} anos em {} e ainda faltam {} anos para o alistamento.".format(nasc, idade, atual, saldo))
elif idade > 18:
    saldo = idade - 18
    print("Quem nasceu em {} tem {} anos em {} e já devia ter se alistado há {} anos.".format(nasc, idade, atual, saldo))

