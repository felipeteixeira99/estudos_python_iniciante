

# Por que strings são imutaveis ?

x = ' banana '
print(x)
print(x.split('n'))
print(x.strip())
print(dir(x))


x = 'texto'
print(x[1].upper())
print(x)

x[1] = 'e'

x = 'texto'
print(x)
x = 'pera'
print(x)

print(x.upper())