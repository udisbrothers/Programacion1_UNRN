nombres = [" mara ", "TOMAS", "  luCIA", "mARcos  ", " SOFIA "]
nombres_normalizados = []

for n in nombres:
    nombres_normalizados.append(n.strip().casefold().capitalize())
print(nombres_normalizados)