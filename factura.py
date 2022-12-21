from persona import Persona
from factura_detalle import FacturaDetalle

class Factura:
    """clase que implementa factura"""



    def __init__(self, numero: int, cliente: Persona):
        self.serie: str = "f001"
        self.numero: int = numero
        self.cliente: Persona = cliente
        self.base_imponible: float = 0.00
        self.igv: float = 0.00
        self.total: float = 0.00
        self.detalle: FacturaDetalle = []
        pass

    def convertir_a_string(self):
        return print("| {} | {} | {} | {} | {} | {} | {} |".format(self.serie, self.numero, self.cliente.dni, self.cliente.nombres, self.base_imponible, self.igv, self.total))

    
    def converti_foramto_factura(self):
        print("=========================================")
        print("|    factura panaderia 3 ositos         |")
        print("|serie: ", (self.serie))
        print("|datos del cliente:                                         ")
        print(f'|nombre: ', (self.cliente.nombres)                               )
        print(f'|DNI: ', (self.cliente.dni)                              )
        print(f'|base imponible: ',(self.base_imponible)      )
        print(f'|IGV: ',(self.igv)                     ) 
        print(f'|total: ',(self.total)              )                  


    def calcular_totales(self):
        for detalle in self.detalle:
            self.base_imponible = self.base_imponible+detalle.base_imponible
            self.igv = self.igv+detalle.igv
            self.total = self.total+detalle.total
