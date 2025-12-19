numero = int(input('Digite um numero: '))

# O parametro tres por padrão ja é um então não é necessario passar quando o passo for diferente de 1
for n in range(1, 11, 1):
    print(f'{numero} x {n} = {numero * n}')