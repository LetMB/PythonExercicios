#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(l, c):
    area = l * c
    print(f"A área do terreno é de {area} m² ")


l = float(input("Largura (m): "))
c = float(input("Comprimento (m): "))
area(l, c)