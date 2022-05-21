# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

pessoa = {}
galera = []
soma = média = 0
while True:
    pessoa.clear()
    pessoa["nome"] = str(input("Nome: "))
    while True:
        pessoa["sexo"] = str(input('Sexo [M/F]: ' )).upper()[0]
        if pessoa["sexo"] in "MF":
            break
        print("ERRO! Digite apenas M ou F.")
    pessoa["idade"] = int(input("Idade: "))
    soma += pessoa["idade"]
    galera.append(pessoa.copy())
    while True:
        opção = str(input("Quer continuar? [S/N] ")).upper()[0]
        if opção in "SN":
            break
        print("ERRO! Responda apenas S ou N.")
    if opção == "N":
        break
print("=-"*30)
print(galera)
print(f"Foram {len(galera)} pessoas cadastradas.")
média = soma / len(galera)
print(f"A média das idades foi de {média:5.2f} anos.")
print("As mulheres cadastradas foram: ",end="")
for p in galera:
    if p["sexo"] in "Ff":
        print(f"{p['nome']} ", end="")
print()
print("Lista das pessoas que estão acima da média: ")
if p in galera:
    if p["idade"] >= média:
        print("    ")
        for k, v in p.items():
            print(f"{k} = {v}; ", end="")
        print()
print("ENCERRADO!")