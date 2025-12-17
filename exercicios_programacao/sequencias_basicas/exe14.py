v_diaria = 90
km = 0.20

qtd_dias = int(input('Quandidade de dias com o carro: '))
qtd_km = float(input('Digite a quantidade de KM percorrido: '))

valor_total = (qtd_dias * v_diaria) + (qtd_km * km)

print('O valor total das diarias é de: R$', qtd_dias * v_diaria)
print('O valor total do KM é de: R$', qtd_km * km)
print('O valor total do veiculo ficou em: R$', valor_total)
