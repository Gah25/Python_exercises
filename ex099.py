from time import sleep

def maior(* numeros):
    contador = maior = 0
    print('Analisando os valores passados...: ')
    print('=-' * 30)

    for valor in numeros:
        print(f'{valor} ', end='')
        sleep(0.3)
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    print(f'Foram informados {contador} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()