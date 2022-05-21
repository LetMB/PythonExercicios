#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
vitoria = 0
print("=-=- JOGO PAR OU ÍMPAR -=-=")
while True:
    jogador = int(input("Digite um valor: "))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("Você quer par ou ímpar? [P/I] ")).strip().upper()[0]
    print(f"Você jogou {jogador} e o computador jogou {computador}. Total de {total}.")
    print("Deu par!" if total % 2 == 0 else "Deu impar!")
    if tipo == "P":
        if total % 2 == 0:
            print("Você venceu")
        else:
            print("Você perdeu!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("Você venceu!")
            vitoria += 1
        else:
            print("Você perdeu!")
            break
    print("Vamos jogar novamente...")
print(f"Game Over! Você venceu {vitoria} vezes.")