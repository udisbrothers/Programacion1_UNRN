codigo_ingresado = input("Ingrese el codigo: ")

if codigo_ingresado.count("-") == 1:
    lista_codigo = codigo_ingresado.strip().split("-")
    pd = lista_codigo[0]
    sd = lista_codigo[1]
    if pd.isalpha() and sd.isnumeric():
        print(codigo_ingresado.upper())
else:
    print("El codigo ingresado no es valido.")



    
