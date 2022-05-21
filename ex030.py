#Faça um programa que leia se um número inteiro é par ou ímpar

num = int(input("Digite um número qualquer: "))
resultado = num % 2
if resultado == 0:
    print("O número {} é PAR.".format(num))
else:
    print("O número {} é ÍMPAR.".format(num))
