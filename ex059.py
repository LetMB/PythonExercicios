#Crie um programa que leia dois valores e mostre um menu ta tela. Seu programa vai realizar a operação solicitada em casa caso.

from time import sleep
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
opção = 0
print("=-"*12)
while opção != 5:
    print(" ESCOLHA UMA OPÇÃO ")
    print("[ 1 ] SOMAR")
    print("[ 2 ] MULTIPLICAR")
    print("[ 3 ] MAIOR")
    print("[ 4 ] NOVOS NÚMEROS")
    print("[ 5 ] SAIR DO PROGRAMA")
    print("=-"*12)
    opção = int(input("Sua escolha: "))
    if opção == 1:
       soma = n1 + n2
       print("{} + {} = {}".format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print("{} x {} = {}".format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            print("{} é maior que {}.".format(n1, n2))
        else:
            print("{} é maior que {}.".format(n2, n1))
    elif opção == 4:
        print("Informe os números novamente:")
        n1 = int(input("Primeiro valor:"))
        n2 = int(input("Segundo valor:"))
    elif opção == 5:
        print("Finalizando...")
    else:
        print("Opção inválida. Tente novamente!")
    sleep(2)
print("Fim do programa!")
