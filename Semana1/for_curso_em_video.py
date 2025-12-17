for c in range(1,6):
    print('oi')
print('Fim')


for c in range(0,9,2):
    print(c)
print('FIM')

n = int(input('Digite o inicio: '))
f = int(input('Digite o fim:'))
p = int(input('Digite o passo: '))

# O n + 1 vai fazer com que o contador conte ate o ultimo numero 
# uma vez que o python ignora o ultimo numero
for c in range(n, f+1, p ):
    print(c)
print('Fim')

