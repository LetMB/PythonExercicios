#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

contidade = homens = mulher20anos = 0

while True:
    print("--- CADASTRO DE PESSOA ---")
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "FM":
        sexo = str(input("Sexo: ")).strip().upper()[0]
    print("-"*25)
    opção = " "
    while opção not in "SN":
        opção = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if idade > 18:
        contidade += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulher20anos += 1
    if opção != "S":
        break
print(f"Foram cadatradas {contidade} pessoas com mais de 18 anos")
print(f"Foram cadastrados {homens} homens.")
print(f"Foram cadastradas {mulher20anos} mulheres com menos de 20 anos.")