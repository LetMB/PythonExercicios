#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

numeros = []
for cont in range(0,5):
    num = int(input("Digite um valor: "))
    if cont == 0 or num > numeros[-1]:
        numeros.append(num)
        print("Adicionado no final da lista!")
    else:
        pos = 0
        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos,num)
                print(f"Adicionado na posição {pos} da lista!")
                break
            pos += 1

print("-"*40)
print(f"Os valores adicionados em ordem foram: {numeros}")