
contador = 0
for n in range (1,7):
    ano_nascimento = int(input('Digite o ano de nascimento: '))
    if (2025 - ano_nascimento) >= 18:
        contador += 1

print('Quantidade de pessoas maiores de idade: ', contador)