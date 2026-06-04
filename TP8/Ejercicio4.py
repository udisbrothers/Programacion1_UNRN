archivo = open("temperaturas.txt","r")
temperaturas = {}

for linea in archivo:
    ciudad, temperatura = linea.strip().split(";")

    if ciudad not in temperaturas:
        temperaturas[ciudad] = []
    temperaturas[ciudad].append(int(temperatura))

archivo.close()

print(temperaturas)
