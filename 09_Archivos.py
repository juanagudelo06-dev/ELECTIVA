# Online Python compiler (interpreter)
# Write and run Python online using this editor.


#notas.txt
#r read leer
#w write escribir
#a append agregar
#archivo=open("saludo.txt")
#contenido=archivo.read()
#print(contenido)
#archivo.close()
#with open("saludo.txt","r")as archivo:
#  texto=archivo.read()
#print (texto)

#with open("datos.txt", "w") as archivo:
#  archivo.write("Ana")
#with open("datos.txt", "r") as archivo
#  texto=archivo.read()
#print(texto)
# with cierra el archivo al colocar la identación

#para agregar uso "a" append pero debo tener un archivo.
#with open("registro.txt", "w") as archivo:
#  archivo.write("Ana\n")
#with open("registro.txt", "a") as archivo:
#  archivo.write("luis\n")
#  archivo.write("Carlos\n")
#with open("registro.txt", "r") as archivo:
#  leer=archivo.read()
#print(leer)

#leer linea por linea en un archivo
#with open("registro.txt", "r")as archivo:
#  for linea in archivo:
#    print(linea.strip())#strip elimina saltos de linea y espacios
#print("final")

#with open("edades.txt", "w") as archivo:
#  archivo.write("20\n")
#with open("edades.txt", "a") as archivo:
#  archivo.write("25\n")
#  archivo.write("30\n")
#with open("edades.txt", "r") as archivo:
#  for linea in archivos:
#    edad=int(linea.strip())
#    print(edad+5)
#print("fin")

#readlines lee linea por linea 
#with open("registro.txt", "r") as archivo:
#  datos=archivo.readlines()
#print(datos[1].strip())

#listas 
#productos = ["Mouse", "Teclado", "Monitor"]

#with open("productos.txt", "w") as archivo:
#  for producto in productos:
#    archivo.write(producto+"/n")

#nombres=["Ana\n", "Luis\n", "Carlos\n"]
#with open("nombes.txt", "w") as archivo:
#  archivo.writelines(nombres)

#productos=[
#  {"nombre": "Mouse", "precio": 50000, "cantidad": 5},
#  {"nombre": "Teclado", "precio": 80000, "cantidad": 3}  
#]
#with open("productos.txt", "w") as archivo:
#  for producto in productos:
#    archivo.write(producto["nombre"] + "," +
#                  str(producto["precio"]) + "," +
#                  str(producto["cantidad"])+"\n")
#importante a la hora de crear modificar se realiza como str para leerlo se realiza bien sea con int, float o str dependiendo lo que necesite 

#linea="Teclado,80000,3"
#datos=linea.strip().split(",")
#nombre=datos[0]
#precio=int(datos[1])
#cantidad=int(datos[2])

#total=precio*cantidad

#print(datos)
#print(nombre)
#print(precio)
#print(cantidad)
#print(total)
