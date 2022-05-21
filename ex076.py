#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ("Lápis", 2,
            "Borracha", 3,
            "Caderno", 19.90,
            "Estojo", 11.90,
            "Compasso", 6.7,
            "Mochila", 75.90,
            "Caneta", 4.50,
            "Livro", 40)

print("-"*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print("-"*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end="")
    else:
        print(f"R${listagem[pos]:>7.2f}")
print("-"*40)