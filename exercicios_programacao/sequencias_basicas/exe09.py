# 9) Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) 
# e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45. 

real = float(input('Quantos R$ você possui na carteira ? '))
dolar = 5.42
conversao = real / dolar

print(f"Com R${real} você pode comprar ${conversao:.2f}")