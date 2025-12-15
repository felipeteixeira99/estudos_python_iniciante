# 10) Faça um algoritmo que leia a largura e altura de uma parede, calcule e 
# mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, 
# sabendo que cada litro de tinta pinta uma área de 2metros quadrados. 

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
metro_quadrado = largura * altura
tinta = 2
qtd_tinta_gasta = metro_quadrado / tinta

print(f'A parede possui {metro_quadrado:.2f}m2')
print(f'Serão necessários para pintar a parede {qtd_tinta_gasta} litros de tinta')