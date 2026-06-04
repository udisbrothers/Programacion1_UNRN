mediciones = [
    ("temp", 18.5, "Aula 1"),
    ("humedad", 40, "Aula 1"),
    ("temp", 21.0, "Laboratorio"),
    ("presion", 1012, "Laboratorio"),
    ("humedad", 55, "Aula 2")
]

diccionario = {}
tipos = set()
lista = []

for tipo,valor,ubicacion in mediciones:
    tipos.add(tipo)
    lista.append(valor)
    diccionario[ubicacion] = []

for tipo, valor, ubicacion in mediciones:
    diccionario[ubicacion].append((tipo,valor))
    
print(lista)
print(tipos)
print(diccionario)