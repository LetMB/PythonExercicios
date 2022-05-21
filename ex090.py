#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

dic = {}
dic["Nome"] = str(input("Nome: "))
dic["Média"] = float(input(f"Média de {dic['Nome']}: "))

if dic['Média'] >= 7:
    dic['Situação'] = "Aprovado"
elif 5 <= dic['Média'] < 7:
    dic['Situação'] = "Recuperação"
else:
    dic['Situação'] = "Reprovado"
print("-"*30)
for k, v in dic.items():
    print(f"{k} é igual a {v}")