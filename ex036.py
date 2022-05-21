#Escreva um programa para aprovar um mprestimo bancario de uma casa. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado.

valor = float(input("Qual é o valor da casa? R$"))
salario = float(input("Qual é o valor do seu salário? R$"))
anos = int(input("Em quantos anos você pretende pagar? "))

if (valor / (anos * 12)) <= salario * 0.3:
    taxa = (valor / (anos * 12))
    print("Seu empréstimo foi aprovado! Você deverá pagar uma taxa de {:.2f} reais mensais.".format(taxa))
else:
    taxa = (valor / (anos * 12))
    print("Infelizmente o seu empréstimo não foi aprovado porque a taxa de {:.2f} reais excede 30% do seu salário!".format(taxa))