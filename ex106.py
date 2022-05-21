#Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

from time import sleep

c = ("\033[m", #0 - sem cor
    "\033[0;30;41m", #1 - vermelho)

def ajuda(com):
    título(f"Acessando o manual do comando \"{com}\"", 4)
    print(c[6], end="")
    help(com)
    print(c[0], end="")
    sleep(0.3)

def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end="")
    print("="*tam)
    print(f" {msg} ")
    print("="*tam)
    print(c[0], end="")
    sleep(0.5)

comando = ""
while True:
    título("SISTEMA DE AJUDA PYHELP")
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
título("Até logo!", 1)



