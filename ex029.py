#Escreva um programa que leia a velocidade de um carro. Se passar dos 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar 7.00 reais por cada km acima do limite

vel = float(input("Qual a velocidade atual do carro? "))
if vel > 80:
    mul = (vel - 80) * 7
    print("Você está dirigindo acima do limite permitido e foi multado em {:.2f} reais.".format(mul))
else:
    print("Dirija com cuidado!")