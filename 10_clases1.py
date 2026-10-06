# archivos segunda parte
#productos=[
#  {"nombre": "Mouse", "precio": 50000, "cantidad": 5},
#  {"nombre": "Teclado", "precio": 80000, "cantidad": 3}  
#  {"nombre": "Monitor", "precio": 700000, "cantidad": 2}
#]

#with open("productos.txt", "w") as archivo:
#  for producto in productos:
#    archivo.write(producto["nombre"] + "," +
#                  str(producto["precio"]) + "," +
#                  str(producto["cantidad"])+"\n")
#archivo lista de diccionarios
#productos=[]

#with open("productos.txt", "r") as archivo:
#  for linea in archivo:
#    datos=linea.strip().split(",")

#    productos={
#      "nombre": datos[0],
#      "precio": int(datos[1]),
#      "cantidad": int(datos[2]),
#    }
#    productos.append(productos)
#print (productos)

#with open("estudiantes.txt", "w") as archivo:
#  for i in range(3):
#    nombre= input("Ingrese el nombre del estudiante: ")
#    edad= int(input("ingrese la edad: "))
#    archivo.write(nombre + "," + str(edad) + "\n")

#estudiantes=[]

#with open("estudiantes.txt", "r") as archivo:
#  for linea in archivo:
#    datos=linea.strip().split(",")

#    estudiante={
#      "nombre": datos[0],
#      "edad": int(datos[1])
#    }
#    estudiantes.append(estudiante)
#print(estudiantes)
#Programación orientada a objetos(Poo)
#Clase(algo genereral producto) y objeto(algo especifico mouse)

#class Producto:
#  pass
#mouse=Producto()
#teclado=Producto()

#print(type(mouse))

#_init_  se ejecuta automaticamente cuando creamos un objeto

#class Producto:
#  def _init_(self, nombre, precio):
#    self.nombre=nombre
#    self.precio=precio

#mouse=Producto("Mouse",50000)

#class Producto:
#  def __init__(self, nombre, precio, cantidad):
#      self.nombre = nombre
#      self.precio = precio
#      self.cantidad = cantidad
#teclado= Producto ("teclado", 80000, 3)

#print(teclado.precio)

#metodos son funciones

#class Producto:
#  def __init__(self, nombre, precio):
#    self.nombre=nombre
#    self.precio=precio

#  def mostrar_precio(self):
#    print(self.nombre, self.precio)
    
#mouse=Producto("Mouse", 20000) 

#mouse.mostrar_precio()
