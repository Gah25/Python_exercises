tabela_brasileiro = ('Botafogo', 'Flamengo', 'Palmeiras', 'Grêmio', 'Fluminense', 'Bragantino', 'Athletico-PR', 'São Paulo', 'Cuiabá', 'Cruzeiro', 'Fortaleza', 'Internacional', 'Atlético-MG', 'Corinthians', 'Santos', 'Goiás', 'Bahia', 'Coritiba', 'América-MG', 'Vasco da Gama')

print(f'{tabela_brasileiro[0:5]}', '\n')
print(f'{tabela_brasileiro[-4:]}','\n')
print(f'{sorted(tabela_brasileiro)}','\n')
print(f'São Paulo está na {tabela_brasileiro.index("São Paulo")+1}° posição')


# for posicao, time in enumerate(tabela_brasileiro):
#     if time == 'São Paulo':
#         (print(f'{time} {posicao}° - Colocado'))