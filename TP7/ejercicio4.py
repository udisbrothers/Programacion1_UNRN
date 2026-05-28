edad = input("Edad?")
edad.strip()
if edad.isnumeric():
    if 125 > int(edad) > 0 :
        print("La edad registrada es:", edad)
    else:
        print("la edad es menor a 0 o mayor a 125")
else:
    print("el dato ingresado es incorrecto")