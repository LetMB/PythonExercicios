#Faça um programa que calcule a some entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500

s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
print("A soma de todos os números ímpares divisíveis por 3 entre 1 e 500 é {}.".format(s))