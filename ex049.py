#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher

n = int(input("Escolha um número para saber sua tabuada: "))

for c in range(1, 11):
    print("{} x {} = {}".format(n, c, n*c))

