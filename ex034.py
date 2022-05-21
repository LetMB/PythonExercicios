#Escreva um programa que pergunte o salário do funcionário e calcule o seu aumento. Se superior a 1250 reais, calcule aumento de 10%. Se inferior ou igual, o aumento é de 15%.

salario = float(input("Qual o salário do funcionário? "))
if salario > 1250:
    aumento = salario * 1.1
    print("Quem ganhava {:.2f} reais, passa a ganhar {:.2f} reais.".format(salario,aumento))
else:
    aumento = salario * 1.15
    print("Quem ganhava {:.2f} reais, passa a ganhar {:.2f} reais.".format(salario,aumento))