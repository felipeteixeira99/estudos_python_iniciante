frase = str(input('Digite uma frase: ')) # entrada do usuario
palavras = frase.split() # separa as palavras usando o espaço como separador
print(palavras) # printando as palavras
junto = ''.join(palavras) # junta as palavras sem espaço
print(junto) # printa 
inverso = '' # cria uma variavel vazia

# laco
# letra vai iterar da ultima letra ate a primeira de um em um (-1 para pegar do final pro inicio)
# usamos o operador de atribuição composta += que faz o mesmo que v = v + n porem mais rapido
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
# printamos de novo a informação
print(inverso)

# verifica se a as duas variaveis possuem os mesmos valores
if inverso == junto:
    print('E um palidromo')
else:
    print('Não é palidromo')