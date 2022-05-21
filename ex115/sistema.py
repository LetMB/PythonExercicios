from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = "Cursoemvideo.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["Ver pessoas cadastradas","Cadastrar nova Pessoa","Sair do Sistema"])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        print("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print("Saindo do sistema...Até logo!")
        break
    else:
        print("ERRO! Digite uma opção válida!")