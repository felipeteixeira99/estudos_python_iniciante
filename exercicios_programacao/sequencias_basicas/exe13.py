# 13) Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o 
# seu novo salário, com 15% de aumento. 

s = float(input('Salario do colaborador: '))
s_aumento = s + (s * 15) / 100

print('Parabens o seu novo salario é: R$', s_aumento)