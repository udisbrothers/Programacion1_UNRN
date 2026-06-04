lista = []
while len(lista) < 4:
    n = input("nombre?").capitalize().strip(" ")
    if n != "":
        lista.append(n)
    else:
        print("El nombre no puede estar vacio")

archivo = open("nombres.txt","a")
for nombres in lista:
    archivo.write(nombres + ("\n"))
archivo.close()

print(lista)