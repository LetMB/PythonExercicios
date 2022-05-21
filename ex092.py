#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

pessoa = {}
pessoa["nome"] = str(input("Nome: "))
nasc = int(input("Ano de nascimento: "))
pessoa["idade"] = datetime.now().year - nasc
pessoa["ctps"] = int(input("Carteira de trabalho [digite 0 se não tiver]: "))
if pessoa["ctps"] != 0:
    pessoa["contratação"] = int(input("Ano de contratação: "))
    pessoa["salário"] = float(input("Salário: R$"))
    pessoa["aposentadoria"] = pessoa["idade"] + (pessoa["contratação"] + 35) - datetime.now().year
print("=-"*20)
for k, v in pessoa.items():
    print(f" - {k} tem o valor {v}")