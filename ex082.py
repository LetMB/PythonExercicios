#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

completa = []
pares = []
impares = []
while True:
    num = int(input("Digite um valor: "))
    completa.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    opção = str(input("Quer continuar [S/N] ? "))
    if opção in "Nn":
        break
print("-"*30)
print(f"A lista completa é {completa}")
print(f"A lista de pares é {pares}")
print(f"A lista de impares é {impares}")
