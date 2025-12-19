# Desafio: somar numeros multiplos de 3 que são impares de 1 ate 500

# Macete: numero divisivel por 3

soma_total = 0
for n in range(1, 500, 1):
    if n % 3 == 0:
        soma_total += n

print('A soma é ', soma_total)
