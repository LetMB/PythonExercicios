#Faça um programa que leia o IMC e classifique de acordo com o resultado

peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))

IMC = peso / (altura **2)
print("Seu IMC é de {:.1f}!".format(IMC))
if IMC < 18.5:
    print("Você está abaixo do peso!")
elif IMC >= 18.5 and IMC < 25:
    print("Você está no peso ideal!")
elif IMC >= 25 and IMC < 30:
    print("Você está com sobrepeso!")
elif IMC >= 30 and IMC < 40:
    print("Você está obeso!")
elif IMC >= 40:
    print("Você está com obesidade mórbida!")


