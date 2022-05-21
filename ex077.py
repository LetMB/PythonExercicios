#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tupla = ("CANETA", "BOLA", "JACA", "HOJE", "ILHA",
         "RONALDO", "SALSICHA", "COMIDA", "ESCOLA",
         "VIVEIRO", "ABACATE", "ROUPA", "DOCINHO",
         "XADREZ", "PEDRO", "TAMBAQUI", "FLORES")

for palavra in tupla:
    print(f"\nNa palavra {palavra} temos as vogais ", end="")
    for letra in palavra:
        if letra in "AEIOU":
            print(letra, end=" ")