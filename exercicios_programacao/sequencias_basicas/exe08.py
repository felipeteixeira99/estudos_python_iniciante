# 8) Desenvolva um programa que leia uma distância em metros e mostre os valores 
# relativos em outras medidas. 
# Ex:  
# Digite uma distância em metros: 185.72 
# A distância de 85.7m corresponde a: 
# 0.18572Km 
# 1.8572Hm 
# 18.572Dam 
# 1857.2dm 
# 18572.0cm 
# 185720.0mm 

metros = float(input('Digite uma distância em metros: '))
km = metros / 1000
hectometro = metros / 100
decametro = metros / 10
decimetro = metros * 10
centimetro = metros * 100
milimetro = metros * 1000

print(f'A distancia de {metros:.2f}m corresponde a: ')
print(f'{km}km')
print(f'{hectometro}hm')
print(f'{decametro}dam')
print(f'{decimetro}dm')
print(f'{centimetro}cm')
print(f'{milimetro}mm')