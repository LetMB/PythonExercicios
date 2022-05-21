#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = []
while True:
    num = int(input("Adicione um número: "))
    if num not in numeros:
        numeros.append(num)
    else:
        print("Valor duplicado! Não será adicionado!")
    print("Número adicionado com sucesso!")
    opção = str(input("Você quer continuar [S/N]? "))
    if opção in "Nn":
        break
print("-"*40)
numeros.sort()
print(f"Você digitou os números: {numeros}")