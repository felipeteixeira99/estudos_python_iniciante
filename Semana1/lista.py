quadrados = [1,4,9,16,25]
print(quadrados)

print(quadrados[0])
print(quadrados[-1])

print(quadrados[-3])

# suportam contatenação

print(quadrados + [36, 49, 64, 81, 100])

#São mutaveis

cubos = [1,8,27,65,152]
print(cubos)
cubos[3] = 64
print(cubos)


cubos.append(216)
print(cubos)

rgb = ['Vermelho', "Verde", "Azul"]
print(rgb)

rgba = rgb
print(rgba)

print(id(rgb) == id(rgba))
rgba.append("Alf")
print(rgb)
print(rgba)

# Copia

rgb_correto = rgba[:]
print(rgb_correto)
rgb_correto[-1] = "Alfa" # alterar o ultimo elemento da lista
print(rgb_correto)
print(rgba)


letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letras)

letras[2:5] = ['C','D','E']
print(letras)

letras[2:5] = []
print(letras)

letras[:] = []
print(letras)