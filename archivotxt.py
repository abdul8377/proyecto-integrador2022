from io import open
from datetime import date
import random

fecha = date.today()
numero = random.randrange(1, 1000)
iva = 0.21

print(":::::::: Facturación ::::::::\n")

cliente = input("Cliente: ")
servicio = input("Servicio: ")
precio = int(input("Precio: $"))

subtotal = precio * iva
total = precio + subtotal

craer_factura = open(str(fecha)+str(numero)+".txt", "w")
craer_factura.write('''
"Factura #"+numero
"-------------------"
"Cliente: "+cliente
"Servicio: "+servicio
"-------------------"
"Valor: $"+precio
"IVA 21%: $"+subtotal
"-------------------"
"Total: $"total
''')

print("Total: $"+str(total))