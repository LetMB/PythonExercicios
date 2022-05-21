# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

ang = float(input("Digite o ângulo que você deseja: "))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print("Para o ângulo de {}º, o seno é de {:.2f}".format(ang,sen))
print("Para o ângulo de {}º, o cosseno é de {:.2f}".format(ang,cos))
print("Para o ângulo de {}º, a tangente é de {:.2f}".format(ang,tan))