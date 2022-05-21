#Desenvolva um programa que pergunte a distancia de uma viagem. Calcule o preço da passagem, cobrando 0,50 por km para viagens de ate 200km e 0,45 para viagens mais longas

dist = float(input("Qual a distância da sua viagem? "))
print("Você está prestes a começar a sua viagem de {}km.".format(dist))
if dist <= 200:
    preço = dist * 0.5
    print("O preço da sua passagem será de {} reais.".format(preço))
else:
    preço = dist * 0.45
    print("O preço da sua passagem será de {} reais.".format(preço))