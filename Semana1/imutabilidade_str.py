
a = 'chiclete'
b = 'chiclete'

# Não possui alterações
print(a)

print(id(a))
# Não possui alterações
print(b)
print(id(b))
# Aqui alteramos o valor de a no meio do codigo
a = a.capitalize()
print(id(a))

# Mostramos o resultado na tela
print(a)

# Mostramos o valor de B na tela
print(b)

