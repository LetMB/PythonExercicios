#Crie um programa que leia duas notas de um aluno e sua média, mostrando uma mensagem no final, de acordo com a média atingida.

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
média = (n1 + n2)/2

if média >= 7:
    print("Parabéns! Sua média foi de {:.2f} e você está aprovado.".format(média))
elif média >= 5 and média <= 6.9:
    print("Sua média foi de {} e você está de recuperação!".format(média))
elif média < 5:
    print("Infelizmente a sua média foi de {} e você está reprovado.".format(média))