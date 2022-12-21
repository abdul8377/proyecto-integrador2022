from limpiarpantalla import limpiarpantalla
from persona import Persona
from producto import Producto
from factura import Factura

import time
personas: Persona = []
productos: Producto = []
facturas: Factura = []



def crear_persona():
    dni: str = str(input("Ingrese DNI: "))
    nombres: str = str(input("Ingrese Nombres: "))
    apellidos: str = str(input("Ingrese Apellidos: "))
    direccion: str = str(input("Ingrese Direccion: "))
    telefono: str = str(input("Ingrese Telefono: "))
    persona: Persona = Persona(dni, nombres, apellidos, direccion, telefono)
    personas.append(persona)


lista_personas:list=[{"dni":"47259697","nombres":"Noe Wilber","apellidos":"Tipo Mamani","direccion":"UPeU","telefono":"997124032"},
{"dni":"47259698","nombres":"juan","apellidos":" Mamani","direccion":"UPeU","telefono":"997124032"},
{"dni":"47259699","nombres":"pedro","apellidos":"Tipo","direccion":"UPeU","telefono":"997124032"},
{"dni":"47259610","nombres":"Adres","apellidos":"Tipo Mamani","direccion":"UPeU","telefono":"997124032"}]

lista_productos:list=[{"codigo":"01","nombre":"Pan","precio":1.20,"marca":"Union"},
{"codigo":"02","nombre":"Agua","precio":1.00,"marca":"Union"},
{"codigo":"03","nombre":"Paneton","precio":35.00,"marca":"Union"},
{"codigo":"04","nombre":"caramelo","precio":0.50,"marca":"Union"}]

def cargar_datos():
    for persona in lista_personas:
        persona:Persona=Persona(persona["dni"],persona["nombres"],persona["apellidos"],persona["direccion"],persona["telefono"])
        personas.append(persona)
    for producto in lista_productos:
        producto:Producto=Producto(producto["codigo"],producto["nombre"],producto["precio"],producto["marca"])
        productos.append(producto)

def listar_personas():
    for persona in personas:
        Persona.convertir_a_string(persona)


def buscar_persona():
    dni: str = str(input("Ingrese DNI para buscar: "))
    for persona in personas:
        if persona.dni == dni:
            Persona.convertir_a_string(persona)
            return persona


def editar_persona():
    dni: str = str(input("Ingrese DNI para Editar: "))
    for persona in personas:
        if persona.dni == dni:
            persona.nombres = str(input("Ingrese un nuevo nombre: "))


def eliminar_persona():
    dni: str = str(input("Ingrese DNI para Eliminar: "))
    for index, persona in enumerate(personas):
        if persona.dni == dni:
            personas.pop(index)

def clientes():

    continuar: bool = True
    while continuar:

        print("\x1b[1;33m") 
        print("_________________________________________")
        print("|                clientes               |")
        print("|---------------------------------------|")
        print("|                  MENÚ                 |")
        print("|           INGRESE OPCIONES            |")
        print("|      1: PARA AGREGAR cliente          |")
        print("|      2: PARA LISTAR clienteS          |")
        print("|      3: PARA BUSCAR cliente           |")
        print("|      4: PARA EDITAR cliente           |")
        print("|      5: PARA ELIMINAR cliente         |")
        print("|      6: PARA VOLVER                   |")
        print("|_______________________________________|")
        caso: str = str(input("INGRESE OPCIÓN: "))
        match caso:
            case "1":
                limpiarpantalla()
                crear_persona()
                limpiarpantalla()
            case "2":
                limpiarpantalla()
                listar_personas()
                print()
            case "3":
                limpiarpantalla()
                buscar_persona()
            case "4":
                limpiarpantalla()
                editar_persona()
            case "5":
                limpiarpantalla()
                eliminar_persona()
            case "6":
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
    clientes()
