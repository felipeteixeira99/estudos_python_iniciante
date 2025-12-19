import time

"""
Recebe a entrada do usuario
irá contar iniciando do numero inserido para o usuario ate 0
Inicio = numero
Fim =  - 1 (para no zero)
passo = - 1 removendo um  do numero inserido a cada iteração
"""
num = int(input('Digite um numero para a contagem: '))
print('Iniciando a contagem: ')
for n in range(num, -1, -1):
    print(f'Contando {n}')
    time.sleep(1)
print('Fogos')