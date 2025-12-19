# Numeros primos
# Possui exatamente dois divisores sendo eles 1 e o proprio numero

numero = int(input('Digite um numero: '))
contador = 0

for n in range(1, numero + 1):
    if numero % n == 0:
        contador += 1

print('Quantidade de divisores: ', contador)

if contador > 2:
    print('Numero composto')
else:
    print('Numero primo')