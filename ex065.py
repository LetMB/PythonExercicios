#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

média = soma = quant = maior = menor = 0
escolha = "S"
while escolha in "Ss":
    num = int(input("Escolha um valor: "))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    escolha = str(input("Quer continuar [S/N]? ")).upper().strip()[0]
média = soma / quant
print("Você digitou {} números e a média foi {}.".format(quant, média))
print("O maior valor foi {} e o menor valor foi {}.".format(maior, menor))
