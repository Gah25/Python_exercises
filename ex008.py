numero = float(input('Uma distância em metros: '))

km = numero * 0.001
hm = numero * 0.01
dam = numero * 0.1
dm = numero * 10
cm = numero * 100
mm = numero * 1000 

print(f'{km}km')
print(f'{hm}hm')
print(f'{dam:.1f}dam')
print(f'{dm:.0f}dm')
print(f'{cm:.0f}cm')
print(f'{mm:.0f}mm')