salario = float(input('Qual é o salário do Funcionário? R$'))
# -> salario + (salario * 15 / 100) também pode ser feito desse jeito

porcentagem = 15 / 100
salario_real = salario * porcentagem
salario_com_aumento = salario + salario_real

print(f'Um funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R${salario_com_aumento:.2f}')