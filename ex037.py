#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão

num = int(input("Digite um número inteiro: "))
print("Escolha uma das bases para conversão: ")
print("[ 1 ] Converter para binário" )
print("[ 2 ] Converter para octal" )
print("[ 3 ] Converter para hexadecimal")
opção = (int(input("Sua opção: ")))

if opção == 1:
    print("{} convertido para binário é igual a {}.".format(num, bin(num)[2:]))
elif opção == 2:
    print("{} convertido para octal é igual a {}".format(num, oct(num)[2:]))
elif opção == 3:
    print("{} convertido para hexadeciamal é igual a {}".format(num, hex(num)[2:]))
else:
    print("Escolha uma opção válida!")