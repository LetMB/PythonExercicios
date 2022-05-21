#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: – Quantidade de notas      – A maior nota       – A menor nota     – A média da turma     – A situação (opcional)

def notas(*num, sit=False):
    """
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    dic = {}
    dic["Total"] = len(notas)
    dic["Maior"] = max(notas)
    dic["Menor"] = min(notas)
    dic["Média"] = sum(num)/len(num)
    if sit:
        if dic["média"] >= 7:
            dic["Situação"] = "BOA"
        elif dic ["Média"] >= 5:
            dic["Situação"] = "RAZOÁVEL"
        else:
            dic["Situação"] = "RUIM"
    return dic


resp = notas(5.5, 2.5, 8.5)
print(resp)