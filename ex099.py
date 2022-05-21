#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(*num):
    cont = maior = 0
    print("\nAnalizando os valores informados...")
    for valor in num:
        print(f"{valor}", end=" ")
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"Foram informados {cont} valores.")
    print(f"O maior valor foi {maior}.")

maior(2,9,5,4,1)
maior(8,3,2,5)