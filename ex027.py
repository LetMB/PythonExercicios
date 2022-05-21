#Faça um programa que leia o nome completo de uma pessoa, mostrando separadamente o primeiro e ultimo nome dessa pessoa

nome = str(input("Digite o seu nome completo: ")).strip()
n = nome.split()
print("Prazer te conhecer!")
print("Seu primeiro nome é {} ".format(n[0]))
print("Seu último nome é {}".format(n[len(n)-1]))