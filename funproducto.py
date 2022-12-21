from limpiarpantalla import limpiarpantalla
from persona import Persona
from producto import Producto
import time

productos: Producto = []

def crear_producto():
    codigo: str = str(input("Ingtrese Codigo Del Producto: "))
    nombre: str = str(input("Ingtrese Nombre Del Producto: "))
    precio: float = float(input("Ingtrese Precio Del Producto: "))
    marca: str = str(input("Ingtrese Marca Del Producto: "))
    producto: Producto = Producto(codigo, nombre, precio, marca)
    productos.append(producto)


def listar_productos():
    for producto in productos:
        Producto.convertir_a_string(producto)


def buscar_producto():
    codigo: str = str(input("Ingtrese Codigo para buscar  Producto: "))
    for producto in productos:
        if producto.codigo == codigo:
            Producto.convertir_a_string(producto)
            return producto


def editar_producto():
    codigo: str = str(input("Ingtrese Codigo para editar  Producto: "))
    for producto in productos:
        if producto.codigo == codigo:
            Producto.convertir_a_string(producto)
            nombre: str = str(input("Ingrese Nuevo nombre de producto: "))
            producto.nombre = nombre
            Producto.convertir_a_string(producto)


def eliminar_producto():
    codigo: str = str(input("Ingtrese Codigo para eliminar  Producto: "))
    for index, producto in enumerate(productos):
        if producto.codigo == codigo:
            Producto.convertir_a_string(producto)
            productos.pop(index)

def menu_producto():
    from reportlab.pdfgen import canvas
    c = canvas.Canvas("hola-mundo.pdf")
    c.save()

    continuar: bool = True
    while continuar:

        print("\x1b[1;33m") 
        print("_________________________________________")
        print("|               PRODUCTOS               |")
        print("|---------------------------------------|")
        print("|                  MENÚ                 |")
        print("|           INGRESE OPCIONES            |")
        print("|      1: PARA AGREGAR PRODUCTO         |")
        print("|      2: PARA LISTAR PRODUCTOS         |")
        print("|      3: PARA BUSCAR PRODUCTO          |")
        print("|      4: PARA EDITAR PRODUCTO          |")
        print("|      5: PARA ELIMINAR PRODUCTO        |")
        print("|      6: PARA volver                   |")
        print("|_______________________________________|")
        caso: str = str(input("INGRESE OPCIÓN: "))
        match caso:
            case "1":
                limpiarpantalla()
                crear_producto()
                limpiarpantalla()
            case "2":
                limpiarpantalla()
                listar_productos()
                print()
            case "3":
                limpiarpantalla()
                buscar_producto()
            case "4":
                limpiarpantalla()
                editar_producto()
            case "5":
                limpiarpantalla()
                eliminar_producto()
            case "6":
                limpiarpantalla()
                limpiarpantalla()
                print("cargando...")
                time.sleep(1)
                limpiarpantalla()
                break
              
            case _:
                limpiarpantalla()
                print("ingrese de nuevo la opcion")
                time.sleep(1)
                limpiarpantalla()


if __name__ == '__main__':
    menu_producto()
