#Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da PA, usando a estrutura while

print("==== 10 TERMOS DE UMA PA ====")
a1 = int(input("Primeiro termo da PA: "))
razão = int(input("Razão da PA: "))
termo = a1
cont = 1
while cont <= 10:
    print("{} -> ".format(termo), end="")
    termo += razão
    cont += 1
print("FIM")