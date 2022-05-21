#Faça um programa que calcule um valor a ser pago por um produto considerando o seu preço nomral e condições de pagamento

print("=======================")
preço = float(input("Preço das compras: "))
print("FORMAS DE PAGAMENTO")
print("[ 1 ] à vista dinheiro/ cheque")
print("[ 2 ] à vista no cartão")
print("[ 3 ] 2x no cartão")
print("[ 4 ] 3x ou mais no cartão")
opção = int(input("Qual é a opção? "))
if opção == 1:
    novo = preço * 0.9
    print("Sua compra de R${} terá 10% de desconto e fica em R${}.".format(preço, novo))
elif opção == 2:
    novo = preço * 0.95
    print("Sua compra de R${} terá 5% de desconto e fica em R${}.".format(preço, novo))
elif opção == 3:
    parcela = preço / 2
    print("Sua compra será parcelada em 2x de R${} sem juros.".format(parcela))
elif opção == 4:
    parcelas = int(input("Quantas parcelas? "))
    juros = preço * 1.2
    par = juros / parcelas
    print("Sua compra será parcelada em {}x de R${:.2f} com juros.".format(parcelas, par))
    print("Sua compra de R${} vai custar R${} no final.".format(preço, juros))
else:
    print("Digite uma opção válida!")