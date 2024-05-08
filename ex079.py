"""
# JEITO QUE EU FIZ

lista_numerica = []

while True:
    valor = (int(input('Digite um valor: ')))
    if valor not in lista_numerica:
        lista_numerica.append(valor)
        print(f'Valor adicionado com sucesso...')
        resposta = ' '
        while resposta not in 'SN':
            resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resposta == 'N':
            break
    else:
        print('Não é possivel adicionar valores duplicado')
       
print(f'Você digitou os valores {sorted(lista_numerica)}')"""
    

#####################################################################

# JEITO PROFESSOR GUANABARA
numeros = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
numeros.sort()
print(f'Você digitou os valores {numeros}')