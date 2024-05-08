salario = float(input('Qual é o seu sálario:? '))

porcentagem_10 = (10 / 100)
salario_dez_por_cento = (salario * porcentagem_10) + salario

porcentagem_15 = (15 / 100)
salario_quinze_por_cento = (salario * porcentagem_15) + salario

if salario > 1250:
     print(f'Você ganhou um aumento salarial de 10%. O valor do reajuste vai ficar R${salario_dez_por_cento:.2f}')

else:
     print(f'Você ganhou um aumento salarial de 15%. O valor do reajuste vai ficar R${salario_quinze_por_cento:.2f}')

   