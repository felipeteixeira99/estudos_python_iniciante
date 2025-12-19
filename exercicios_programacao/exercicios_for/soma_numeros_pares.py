soma = 0
for n in range(1, 7):
    print(f'Rodada: {n}')
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        soma += numero
print(f'A soma dos numeros pares é {soma}')