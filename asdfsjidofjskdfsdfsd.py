ruta_archivo = "./archivos/gestion_pagos.txt"

def BuscarServicios(codigo):
    servicios = None
    archivoServicio = open(ruta_archivo, "r")
    for linea in archivoServicio.readlines():
        atributo = linea.split(";")
        if codigo == atributo[0]:
            break
    archivoServicio.close()


import sys
nombres = []
precios = []
cantidades_vendidas = []

while True:
    print("""
=================================
           Spa "Cielo"
    No hay Mejor dia que este
=================================
          MENÚ DE PAGO
=================================
""")
    eleccion = input("""
1 - Introducir un Servicio a utilizar
2 - Pagar un Servicio
3 - Emitir voleta o visualizar
4 - Borrar un Servicio Consumido
5 - Borrar todos los Servicios Consumidos
6 - Salir
Seleccione: """)



    if eleccion == "1":
        nombre = input("Nombre del Servicio: ")
        precio = float(input("Precio del Servicio: "))
        cantidad_vendida = 0.0
        nombres.append(nombre)
        precios.append(precio)
        cantidades_vendidas.append(cantidad_vendida)


        
    elif eleccion == "2":
        nombre_servicio = input("Nombre del Servicio Utilizado a Pagar: ")
        if nombre_servicio in nombres:
            cantidad = float(input("Cantidad en horas: "))
            indice = nombres.index(nombre_servicio)
            precio = precios[indice]
            cantidades_vendidas[indice] += cantidad
            print(
                f"Se Usaron(n) {cantidad} {nombre_servicio}. Total: {cantidad * precio}")
        else:
            print("El Servicio no existe")
    elif eleccion == "3":
        if len(nombres) <= 0:
            print("No este servicio")
            continue
        # Los nombres de Productos
        servicio_mas_usado = nombres[0]
        servicio_menos_usado = nombres[0]
        servicio_con_mas_ingresos = nombres[0]
        servicio_con_menos_ingresos = nombres[0]
        # Pero también necesitamos el conteo. Simplemente los inicializamos en un elemento del arreglo
        mas_usado = cantidades_vendidas[0]
        menos_usado = cantidades_vendidas[0]
        con_mas_ingresos = cantidades_vendidas[0] * precios[0]
        con_menos_ingresos = cantidades_vendidas[0] * precios[0]
        print(" ------------------VOLETA DE VENTA---------------------")
        print("+--------------------+----------+----------+----------+")
        print("|NOMBRE              |CANT. HORA    |PRECIO    |IMPORTE  |")
        print("+--------------------+----------+----------+----------+")
        indice = 0
        total = 0
        while indice < len(nombres):
            nombre = nombres[indice]
            precio = precios[indice]
            cantidad_vendida = cantidades_vendidas[indice]
            importe = precio * cantidad_vendida
            print("|{:<20}|{:>10.2f}|{:>10.2f}|{:>10.2f}|".format(
                nombre, cantidad_vendida, precio, importe))
            print("+--------------------+----------+----------+----------+")
            if cantidad_vendida > mas_usado:
                mas_usado = cantidad_vendida
                servicio_mas_usado = nombre
            if cantidad_vendida < menos_usado:
                menos_usado = cantidad_vendida
                servicio_menos_usado = nombre
            if importe > con_mas_ingresos:
                con_mas_ingresos = importe
                servicio_con_mas_ingresos = nombre
            if importe < con_menos_ingresos:
                con_menos_ingresos = importe
                servicio_con_menos_ingresos = nombre
            total += importe
            indice += 1

        print(
            "|--------------------|----------|TOTAL:    |{:>10.2f}|".format(total))
        print("+--------------------+----------+----------+----------+")
        print(
            f"Servicio más requerido: {servicio_mas_usado}, con {mas_usado} unidades")
        print(
            f"Servicio menos Usado: {servicio_menos_usado}, con {menos_usado} unidades")
        print(
            f"Servicio con más ingresos: {servicio_con_mas_ingresos}, con {con_mas_ingresos} soles")
        print(
            f"Servicio con menos ingresos: {servicio_con_menos_ingresos}, con {con_menos_ingresos} soles")
    elif eleccion == "4":
        nombre_Servicio = input("Nombre del Servicio que se elimina: ")
        if nombre_Servicio in nombres:
            indice = nombres.index(nombre_Servicio)
            del nombres[indice]
            del precios[indice]
            del cantidades_vendidas[indice]
            print(f"Se elimina {nombre_Servicio}")
        else:
            print("El Servicio no existe")

    elif eleccion == "5":
        if input("Seguro (s/n): ") == "s":
            nombres = []
            precios = []
            cantidades_vendidas = []

    elif eleccion == "6":
        if input("Seguro (s/n): ") == "s":
            sys.exit()