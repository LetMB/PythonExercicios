#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão

print("====================")
print(" 10 TERMOS DE UMA PA")
print("====================")

a1 = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
a10 = a1 + (9 * razão)

for c in range(a1,a10 + razão,razão):
    print((c), end= " - ")
print("FIM")