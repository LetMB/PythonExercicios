#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = []
for cont in range(0,5):
    numeros.append(int(input(f"Digite o valor da posição {cont}: ")))

print(f"Você digitou: {numeros}")
print(f"O maior valor foi {max(numeros)} digitado na posição {numeros.index(max(numeros))}")
print(f"O menor valor foi {min(numeros)} digitado na posição {numeros.index(min(numeros))}")