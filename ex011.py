#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

l = float(input("Qual a largura da parede? "))
a = float(input("Qual a altura da parede? "))
a = l*a
t = a/2
print("A área a ser pintada é de {:.2f} metros e serão necessários {} litros de tinta para pinta-la.".format(a,t))