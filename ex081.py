
# JEITO QUE EU FIZ

lista = []
contador = 0

while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    lista.sort(reverse=True) # Ordena a lista de forma decrescente
    contador += 1
    resposta = ' '
    if resposta not in 'Ss':
        resposta = str(input('Quer continuar? [S/N] ')).strip()
    if resposta in 'Nn':
        break
print('=-' * 30)
print(f'Foram digitados {contador} elementos')
print(f'{lista}')

if 5 in lista:
    print('O valor 5 foi digitado e está na lista')
else:
    print('O valor 5 não foi digitado, portanto não se encontra na lista')
        
######################################################################

"""
# JEITO PROFESSOR GUANABARA

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N] ')).strip()
    if resposta in 'Nn':
        break
print('=-' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True) # Mostra os valores de forma decrescente
print(f'Os valores em ordem decrescente são {valores}')"""