#Crie um programa que leia o nome completo de uma pessoa e mostre o nome com todas as letras maíusculas e minúsculas, quantas letras ao td e quantas letras tem o primeiro nome

nome = str(input("Digite o seu nome: ")).strip
print("Seu nome em maiúsculas é {}.".format(nome.upper()))
print("Seu nome em minúsculas é {}.".format(nome.lower()))
print("Seu nome tem {} letras.".format(len(nome) - nome.count("")))
print("Seu primeiro nome tem {} letras".format(nome.find(" ")))
