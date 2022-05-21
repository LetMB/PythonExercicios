#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    n = int(input("Quer ver a tabuada de qual valor? "))
    if n < 0:
        break
    print("-"*15)
    for c in range(1,11):
        mult = n * c
        print(f"{n} x {c} = {mult}")
    print("-" * 15)
print("-"*20)
print("Tabuada encerrada!")