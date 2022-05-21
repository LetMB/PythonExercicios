#Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa/ 100)
    return res if formato == False else moeda(res)

def diminuir(preço=0, taxa=0):
    res = preço - (preço * taxa/ 100)
    return res if formato == False else moeda(res)

def dobro(preço=0):
    res = preço * 2
    return res if not formato else moeda(res)

def metade(preço=0):
    res = preço / 2
    return res if not formato else moeda(res)

def moeda(preço = 0, moeda = "R$"):
    return f"{moeda}{preço:>.2f}".replace(".",",")

def resumo(preço=0, taxaa=10, taxa=5):
    print("-"*30)
    print("RESUMO DO VALOR".center(30))
    print("-"*30)
    print(f"Preço analisado: \t{moeda(preço)})
    print(f"Dobro do preço: \t{dobro(preço, True)}")
    print(f"Metade do preço: \t{metade(preço, True)}")
    print(f"{taxaa}de aumento: \t{aumentar(preço, taxaa, True)}")
    print(f"{taxar}% de redução: \t\t{diminuir(preço, taxar, True)}")
    print("-"*30)
