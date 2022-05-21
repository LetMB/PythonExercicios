#Melhore o jogo do desafio 28 onde o computador vai "pensar" em um número entre 0 a 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

from random import randint
PC = randint(0,10)
palpite = int(input("Qual número entre 0 a 10 o PC escolheu? "))
npalpite = 0
while palpite != PC:
    print("Não foi esse número, tente novamente!")
    palpite = int(input("Qual número entre 0 a 10 o PC escolheu? "))
    npalpite += 1
    if palpite == PC:
        print("Parabéns, você adivinhou! Foram necessários {} palpites até descobrir o número.".format(npalpite))