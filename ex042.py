reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
      print('Os segmentos acima PODEM FORMAR um triângulo ', end='')

      if reta1 == reta2 == reta3:
            print('EQUILÁTERO')
      
      elif reta1 != reta2 != reta3 != reta1:
            print('ESCALENO')

      else:
            print('ISÓSCELES')

else:
      print('Os segmentos acima NÃO PODEM FORMAR triângulo')

"""
###JEITO QUE FIZ### TEM UM ERRO EM QUE PRINTA O NOME DO TRIANGULO MESMO NÃO PODENDO SER FORMADO 

print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)

reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
      print('Os segmentos acima PODEM FORMAR um triângulo')
elif
      print('Os segmentos acima NÃO PODEM FORMAR um triângulo')

elif reta1 == reta2 == reta3:
      print('EQUILATERO')
elif reta1 == reta2 != reta3:
      print('ISÓSCELES')
elif reta1 == reta3 != reta2:
      print('ISÓSCELES')
elif reta2 == reta3 != reta1:
      print('ISÓSCELES')
else:
      print('ESCALENO')"""