#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

def sorteia(num):
    print("Sorteando 5 valores da lista: ", end=" ")
    for c in range(0,5):
        n = randint(0,9)
        num.append(n)
        print(f"{n}", end=" ")
        sleep(0.3)
    print("FIM!")

def somaPar(num):
    soma = 0
    for valor in num:
        if valor % 2 == 0:
            soma += valor
    print(f"Somando os valores pares de {num}, temos {soma}.")

numeros = []
sorteia(numeros)
somaPar(numeros)
