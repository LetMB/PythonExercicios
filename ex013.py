#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

s = float(input("Digite o salário do funcionário: R$"))
a = s * 1.15
print("O salário do funcionário, com 15% de aumento, ficou em {:.2f} reais.".format(a))