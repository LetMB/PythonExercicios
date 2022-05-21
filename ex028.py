#Escreva um programa que faça o PC pensar em um número entre 0 e 5 e peça para o usuário descobrir qual foi o número escolhido pelo computador

from random import randint
from time import sleep

n1 = randint(0,5)
n2 = int(input("Tente adivinhar o número que o PC está pensando: "))
print("PROCESSANDO...")
sleep(3)
if n1 == n2:
    print("Parabens, você acertou!")
else:
    print("Que pena, você errou! O PC pensou no número {} e não no {}. ".format(n1,n2))