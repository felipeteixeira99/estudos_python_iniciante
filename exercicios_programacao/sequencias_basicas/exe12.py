# 12) Crie um programa que leia o preço de um produto, calcule e mostre o seu 
# PREÇO PROMOCIONAL, com 5% de desconto. 

preco = int(input('Digite o preço do produto: '))

p_desconto = preco - (preco * 5) / 100
print('O preço com desconto é: R$', p_desconto)