#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo e calcule e mostre o comprimento da hipotenusa

from math import hypot

n1 = float(input("Escreva o comprimento do cateto oposto: "))
n2 = float(input("Escreva o comprimento do cateto adjacente: "))
h = hypot(n1,n2)
print("O comprimento da hipotenusa é de {:.2f}.".format(h))