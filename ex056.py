#Cria um programa que leia o nome, idade e sexo de 4 pessoas e mostre a média de idade do grupo, o nome do homem mais velho e quantas mulheres tem menos de 20 anos

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ""
totmulher20 =0

for c in range(1, 5):
    print("---------{}ª PESSOA---------".format(c))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    if c == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print("A média de idade do grupo é de {} anos".format(mediaidade))
print("O homem mais velho tem {} anos e se chama {}.".format(maioridadehomem, nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos.".format(totmulher20))