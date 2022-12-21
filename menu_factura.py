from limpiarpantalla import limpiarpantalla
from persona import Persona
from producto import Producto
from factura import Factura
from factura_detalle import FacturaDetalle
from cliente import buscar_persona
from funproducto import buscar_producto
from reportlab.pdfgen import canvas
import time
import datetime



personas: Persona = []
productos: Producto = []
facturas: Factura = []



def crear_factura():
    print("Para crear la factura debe buscar un cliente")
    cliente: Persona = buscar_persona()
    factura: factura = Factura(len(facturas)+1, cliente)
    factura.convertir_a_string()
    contuar: bool = True
    while contuar:
        producto: Producto = buscar_producto()
        cantidad: float = float(input("Ingrese la cantidad del producto: "))
        factura.detalle.append(FacturaDetalle(producto.codigo, producto.nombre, cantidad, producto.precio))
        condicion: str = str(input("Escriba SI para seguir agregando producto: "))
        if condicion == "SI":
            contuar = True
        else:
            contuar = False
            factura.calcular_totales()
            facturas.append(factura)
            
        
def listar_facturas():
    print("| SERIE | NUMERO | DNI CLIENTE | NOMBRE CLIENTE | BASE IMPONIBLE | IGV   | TOTAL |")
    for factura in facturas:
        Factura.convertir_a_string(factura)



def guardar_pdf():
    from reportlab.pdfgen import canvas
    c = canvas.Canvas("factura.pdf")
    c.drawString(100,750,listar_facturas())
    c.save()


def buscar_factura():
    numero: int = int(input("Ingrese numero de factura para buscar: "))
    for factura in facturas:
        if factura.numero == numero:
            Factura.converti_formato_factura(factura)
            print("==================================")
            print("| CODIGO | PRODUCTO | CANTIDAD |BASE IMPONIBLE | IGV   | TOTAL |")
            for detalle in factura.detalle:
                FacturaDetalle.convertir_a_string(detalle)

def Editar_comprobante(ruta_archivo, filas, columna, nuevo_dato):
    contenido = list()
    with open(ruta_archivo, "r+") as archivo:
        contenido = archivo.readlines()
        for fila in filas:
            columnas = contenido[fila - 1].split(";")
            columnas[columna] = nuevo_dato
            contenido[fila - 1] = ";".join(columnas) + "\n"
    with open(ruta_archivo, "w") as archivo:
        archivo.writelines(contenido)
        return print("Cambiado correctamente")


def factura_menu():

    continuar: bool = True
    while continuar:

        print("\x1b[1;33m") 
        print("_________________________________________")
        print("|          SISTEMA DE VENTAS            |")
        print("|---------------------------------------|")
        print("|                  MENÚ                 |")
        print("|           INGRESE OPCIONES            |")
        print("|                                       |")
        print("|      1: PARA GENERAR FACTURA          |")
        print("|      2: PARA LISTAR FACTURA           |")
        print("|      3: PARA BUSCAR FACTURA           |")
        print("|      4: PARA volver                    |")
        print("|_______________________________________|")
        caso: str = str(input("INGRESE OPCIÓN: "))
        match caso:
            case "1":
                limpiarpantalla()
                crear_factura()
                limpiarpantalla()
            case "2":
                limpiarpantalla()
                listar_facturas()
                print()
            case "3":
                limpiarpantalla()
                buscar_factura()
            case "4":
                limpiarpantalla()
                print("volviendo...")
                time.sleep(1)
                limpiarpantalla()
                break
                          
            case _:
                limpiarpantalla()
                print("cargando...")
                time.sleep(2)
                limpiarpantalla()




if __name__ == '__main__':
    factura_menu()