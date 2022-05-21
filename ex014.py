#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF

tc = float(input("Digite a temperatura em ºC para ser convertida: "))
tf = ((9*tc)/5)+32
print("{}ºC equivale a {}ºF.".format(tc,tf))