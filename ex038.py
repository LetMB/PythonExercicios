#Escreva um programa que leia dois números inteiros e compareos

n1 = int(input("Escreva o primeiro número: "))
n2 = int(input("Escreva o segundo número: "))

if n1 > n2:
    print("O primeiro número é maior.")
elif n2 > n1:
    print("O segundo número é maior.")
elif n1 == n2:
    print("Os dois números são iguais.")