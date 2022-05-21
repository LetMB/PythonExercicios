#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

from math import trunc

num = float(input("Escreva um número real: " ))
print("O número {} tem a sua parte inteira {}.".format(num, trunc(num)))
