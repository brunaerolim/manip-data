numeros = [255, 256, 257, 258, 259, 260, 261, 262, 263]

for numero in numeros:
    if numero %2 != 0:
        numeros.remove(numero)


print(numeros) 