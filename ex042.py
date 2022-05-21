#Faça um programa que leia três segmentos de reta e classifique o triângulo formado

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os três segmentos formam um triângulo ", end="")
    if r1 == r2 == r3:
        print("equilátero!")
    if r1 == r2 or r2 == r3 or r1 == r3:
        print("isósceles!")
    if r1 != r2 != r3 != r1:
        print("escaleno!")
else:
    print("Os três segmentos não podem formar um triângulo!")
