"""
# JEITO QUE EU FIZ

numero = 1
contador = 0
soma = 0
opcao = 1
maior = float('-inf')

while True:
    numero = int(input('Digite um número "OU" Digite [ 0 ] para parar: '))
    
    if numero == 0:
        break

    contador += 1
    soma = soma + numero
    media = soma / contador
    
    maior = float(input('Digite [ 0 ] para continuar: '))
    if numero > maior:
        maior = numero

    # while opcao != 0:
    #     opcao = int(input('Tecle [ 0 ] para continuar: '))
    #     if opcao == 0:
    

    # print(f'A soma entre todos os valores é: {soma}', end='  ')
    # print(f'A média é: {media:.2f}',)
print(f'O maior número digitado é: {maior}')
print(f'A soma entre todos os valores é: {soma}', end='  ')
print(f'A média é: {media:.2f}',)
"""



# JEITO PROFESSOR GUANABARA

resposta = 'S'
media = quantidade = soma = maior = menor = 0

while resposta in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    quantidade += 1

    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / quantidade
print('Você digitou {} números e a média foi {}'.format(quantidade, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))


#################################################################################

