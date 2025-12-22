# Numeros primos
# Possui exatamente dois divisores sendo eles 1 e o proprio numero


numero = int(input('Digite um numero: '))
contador = 0

# N vai iterar de um ate numero mais um para pegar todo o intervalo
for n in range(1, numero + 1): 
    if numero % n == 0: # se o resto da divisao de numero / n for igual a 0 contador vai ser incrementado
        contador += 1

print('Quantidade de divisores: ', contador)

if contador > 2: # se o contador for maior que zero esse numero não é primo
    print('Numero composto')
else:
    print('Numero primo') # senao numero primo

    