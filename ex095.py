jogador = {}
partidas = []
time = []

while True:
    jogador['Nome'] = str(input('Nome: '))
    total = int(input(f'Quantas partidas o {jogador["Nome"]} jogou? '))
    partidas.clear()
    for c in range(0, total):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    
    while True:
        resposta = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break
print('=-' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('=-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]["Gols"]):
            print(f'     No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
