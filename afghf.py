import pdfkit
serie=input("f001")
numero=input("1")
dni=input("ingrese su dni: ")
nombres=input("ingrese sus noimbres: ")
telefono=input("ingrese su telefono: ")
precio_producto=int(input("ingrese el precio del producto: "))
cant=int(input("ingrese la cantidad: "))

cantidad= cant*precio_producto
base_imponible=(precio_producto*cantidad)/1.18
igv=(precio_producto*cantidad)-base_imponible
total=precio_producto*cantidad



with open("factura.html", "w") as file:
    file.write("<h1>factura de abdul</h1><br>")
    file.write("<h2>producto: pan.</h2><br>")
    file.write("<h3>serie: </h3>: " +str(serie))
    file.write("<h4>numero: </h4>: " +str(numero))
    file.write("<h5>DNI: </h5>: " +str(dni))
    file.write("<h6>nombres: </h6>: " +str(nombres))
    file.write("<h7>telefono: </h7>: " +str(telefono))
    file.write("<h8>precio unitario del producto: </h8>: " +str(precio_producto))
    file.write("<h9>base imponible</h9>: " +str(base_imponible))
    file.write("<h10>igv</h10>: " +str(igv))
    file.write("<h11>total</h11>: " +str(total))
    
exe = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=exe)
pdfkit.from_file("factura.html", "factura.pdf", configuration=config)
print("factura creada")