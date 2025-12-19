termo = int(input('Digite um numero: '))
razao = int(input('Digite a razão: '))

numero = termo
for n in range(1,11):
    print(f'{numero}', end =' > ')
    numero += razao
    