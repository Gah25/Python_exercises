def notas(*n, situacao=False):
    """
     -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor (opcional), indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informções sobre a situação da turma.
    """
    r = {}
    r['Total'] = len(n) 
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if situacao == True:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média']  >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r
# Programa principal
resp = notas(9, 10, 9, 8.5,  situacao=False)
print(resp)
help(notas)