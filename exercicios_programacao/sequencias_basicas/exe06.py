# 6) Faça um programa que leia um número inteiro e mostre o seu antecessor e seu 
# sucessor. 
# Ex:  
# Digite um número: 9 
# O antecessor de 9 é 8 
# O sucessor de 9 é 10

num = int(input('Digite o numero: '))

antecessor = num - 1
sucessor = num + 1

print(f'O antecessor do numero {num} é {antecessor} e o seu sucessor é {sucessor}')