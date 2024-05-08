jogador = {}
partidas = []

jogador['Nome'] = str(input('Nome: '))
total = int(input(f'Quantas partidas o {jogador["Nome"]} jogou? '))

for c in range(0, total):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
print('=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 30)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas')
for i, v in enumerate(jogador['Gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')