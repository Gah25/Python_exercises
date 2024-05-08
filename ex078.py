
# JEITO QUE EU FIZ -> retorna, mas não em uma linha

valores = []
for contador in range(0,5):
    valores.append(int(input('Digite um valor: ')))
print('=-' * 20)
print(valores)

maior_valor = max(valores)
menor_valor = min(valores)

print(f'O maior valor foi: {maior_valor}', end=' ')
for chave, valor in enumerate(valores):
    if valor == maior_valor:
        print(f'{chave}...', end='')
        
print(f'\nO menor valor foi: {menor_valor}', end=' ')
for chave, valor in enumerate(valores):
    if valor == menor_valor:
        print(f'{chave}...', end='')
        
    


"""
# JEITO PROFESSOR GUANABARA
maior = 0
menor = 0

valores = []
for contador in range(0,5):
    valores.append(int(input(f'Digite um valor na posição {contador}: ')))
    if contador == 0:
        maior = menor = valores[contador]
    else:
        if valores[contador] > maior:
            maior = valores[contador]
        if valores[contador] < menor:
            menor = valores[contador]
print('=-' * 20)
print(valores)
print(f'O maior valor digitado foi {maior} ', end='')
for i, v in enumerate(valores):
    if valores[i] == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {menor} ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')"""