#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

tupla = ("0","1","2","3","4","5","6","7","8","9")

numeros = (randint(1,10), randint(1,10), randint(1,10),
     randint(1,10), randint(1,10))

print(f"Foram sorteados os números: ", end="")
for n in numeros:
    print(f"{n} ", end="")

print(f"\nO maior valor sorteado foi {max(numeros)}")
print(f"O menor valor sorteado foi {min(numeros)}")