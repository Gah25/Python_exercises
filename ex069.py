print('-' * 20)
print('CADASTRE UMA PESSOA')
print('-' * 20)

anos = 0
homens = 0
mulheres_menos_20_anos = 0


while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    
    if idade >= 18:
        anos += 1 
    
    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade < 20:
        mulheres_menos_20_anos += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break 

print(f'Total de pessoas com mais de 18 anos: {anos}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres_menos_20_anos} mulheres com menos de 20 anos')