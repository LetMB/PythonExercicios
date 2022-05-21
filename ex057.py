#Faça um programa que leia o sexo de uma pessoa, mas sí aceite M ou F. Caso esteja errado, peça a digitação novamente até ter um valor correto

sexo = str(input("Digite o sexo [F/M]: ")).strip().upper()[0]
while sexo not in "MmFf":
    print("Digite um sexo válido!")
    sexo = str(input("Digite o sexo [F/M]: ")).strip().upper()[0]
print("Sexo registrado com sucesso!")
