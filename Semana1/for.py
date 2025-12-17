# For

palavras = ['gato', 'janela', 'defenestrar']
for p in palavras:
    print(p, len(p))


# Coleção de dados
    users = {'Hans': 'active', 'Eleonore': 'inactve', 'Felipe': 'active'}

# Iterar por uma copia
    for user, status in users.copy().items():
        if status == 'inactve':
            del users[user]

# Estrategia recomendada

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

# funcao range
for i in range(5):
    print(i)

# Ponto de partida ja comeca com 5 apresentado os valores de 5 a 9
list(range(5,10))
print()

# Comeca com 0, pula de 3 em 3 ate 10
print(list(range(0,10,3)))

# Comeca com -10, precisa ir ate -100 pulando de -30
print(list(range(-10,-100,-30)))

# Recebe uma lista
# i vai iterar sobre o tamanho da lista
a = ['Maria', 'tinha', 'um', 'carneirinho']
for i in range(len(a)):
    print(i, a[i])

# break e continue
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(f"{n} igual a {x} * {n//x}")
            break

for n in range(2,10): # comeca o range com 2 e vai ate 10
    print('Valor atual de n',n)
    for x in range(2,n):
        print('Valor atual de x',x)
        print('Divisao x / n e ', n % x)

