soma_idade = 0
media = float(0)
nome_pessoa_mais_velha = str('') 
idade_pessoa_mais_velha = int(0)
qtd_mulheres = 0

for p  in range(1,6):
    print('=' * 12 + '+' + '=' * 12)
    print(f'{p}° pessoa:')
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: '))

    soma_idade += idade

    if(p == 1):
        nome_pessoa_mais_velha = nome
        idade_pessoa_mais_velha = idade
    else:
        if idade > idade_pessoa_mais_velha:
            nome_pessoa_mais_velha = nome
            idade_pessoa_mais_velha = idade
    
    if (sexo == 'F' or 'f') and idade < 20:
        qtd_mulheres += 1

media = soma_idade / p
print(f'A média de idade do grupo de pessoas é de {media} anos de idade')
print(f'A pessoa mais velha do grupo possui {idade_pessoa_mais_velha} anos de idade e se chama {nome_pessoa_mais_velha}')
print(f'Ao todo são {qtd_mulheres} mulhere(s) com menos de 20 anos de idade')