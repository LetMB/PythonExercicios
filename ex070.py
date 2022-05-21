#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

soma = p1000 = menor = cont = 0
barato = " "

print("=-"*10)
print("   LOJA DA LELET   ")
print("=-"*10)
while True:
    produto = str(input("Nome do produto: "))
    preço = float(input("Preço: R$"))
    cont += 1
    soma += preço
    if preço > 1000:
        p1000 += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    opção = " "
    while opção not in "SN":
        opção = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if opção == "N":
        break

print(f"O total da compra foi de {soma} reais.")
print(f"Temos {p1000} produto(s) custando mais de 1.000,00 reais")
print(f"O produto mais barato foi {barato} que custa {menor} reais.")