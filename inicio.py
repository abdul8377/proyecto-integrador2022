from limpiarpantalla import limpiarpantalla
from cliente import clientes
from funproducto import menu_producto
from menu_factura import factura_menu
import time


def main():

    continuar: bool = True
    while continuar:
    
        print("\x1b[1;33m") 
        print("____________________________")
        print("|      MENU DE INICIO      |")
        print("|--------------------------|")
        print("|[1] clientes              |")
        print("|[2] productos             |")
        print("|[3] factura               |")
        print("|[0] Salir                 |")
        print("|__________________________|")
        
        caso: str = str(input("INGRESE OPCIÓN: "))
        match(caso):
            case "1":
                limpiarpantalla()
                clientes()
                limpiarpantalla()
            case "2":
                limpiarpantalla()
                menu_producto()
                limpiarpantalla()
            case "3":
                limpiarpantalla()
                factura_menu()
                limpiarpantalla()
            case "0":
                limpiarpantalla()
                time.sleep(1)
                limpiarpantalla()
            case _:
                limpiarpantalla()
                print("cargando...")
                time.sleep(1)
                limpiarpantalla()

                
            


if __name__ == '__main__':
    main()



