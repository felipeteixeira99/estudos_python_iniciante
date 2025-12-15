# 11) Desenvolva uma lógica que leia os valores de A, B e C de uma equação do 
# segundo grau e mostre o valor de Delta.

a = int(input('Valor de A: '))
b = int(input('Valor de B: '))
c = int(input('Valor de C: '))

delta = (b * b) - (4 * a * c)
print(delta)
