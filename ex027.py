nome = str(input('Digite seu nome completo: ')).strip().split()

print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu ultimo nome é {nome[-1]}') # ou [len(nome) - 1] 