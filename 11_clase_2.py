# #10_clases_2.py
# class Producto:
#   def __init__(self, nombre, cantidad):
#     self.nombre=nombre
#     self.cantidad=cantidad  
#   def agregar_stock(self, unidades):
#     self.cantidad += unidades
#     def calcular_total(self, precio):
#         return self.precio*precio

# celular=Producto("Celular", 2)
# #celular.agregar_stock(5)

# teclado=Producto("Teclado", 3)
# #Teclado.agregar_stock(5)
# mouse=Producto("mouse", 5)
# mouse.agregar_stock(5)
# monitor=Producto("Monitor", 2)
# #Monitor.agregar_stock(5)


# print(celular.cantidad)
# print(teclado.cantidad)
# print(mouse.cantidad)
# print(monitor.cantidad)

# class Producto:
#   def __init__(self, nombre, precio):
#     self.nombre=nombre
#     self.precio=precio  
#   def agregar_stock(self, unidades):
#     self.precio += unidades
#   def calcular_total(self, cantidad):
#     return self.precio*cantidad

# celular=Producto("Celular", 20000)
# teclado=Producto("Teclado", 35000)
# mouse=Producto("mouse", 50000)
# monitor=Producto("Monitor", 20000)
# mouse.calcular_total(5)

# # print(celular.cantidad)
# # print(teclado.cantidad)
# print(mouse.calcular_total(5))
# # print(monitor.cantidad)

# Producto={
#     "nombre":"Mouse",
#     "precio": 50000
# }

# print(Producto["precio"])

# class Producto: #despues de crear la clase y los metodos creo un objeto
#     def __init__(self, nombre, precio, cantidad):#parametros
#         self.nombre =nombre#parametros (self.nombre= atributos)
#         self.precio=precio#parametros
#         self.cantidad=cantidad#parametros
        
#     def mostrar_datos(self): # def metodoos 
#         return f"{self.nombre} - {self.precio} - {self.cantidad}"
#     def calcular_total(self): # def metodoos
#         return self.precio*self.cantidad
# #para crear un objeto se pone el nombre del objeto=clase(parametros)

# teclado=Producto("teclado", 80000, 2)
# mouse=Producto("mouse", 50000, 3)
# monitor=Producto("monitor", 50000, 3)

# print(mouse.mostrar_datos())
# print(teclado.calcular_total())
# # mouse.agregar_stock(2)

#reto final

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular=titular
        self.saldo=saldo
    def retirar(self, cantidad):
        if cantidad>0 and cantidad<=self.saldo:
            self.saldo=self.saldo-cantidad
    def mostrar_datos(self):
        return f"{self.titular} - {self.saldo}"
    def depositar(self, cantidad):
        if cantidad>0:
            self.saldo+=cantidad
    def consultar_saldo(self):
        return self.saldo
cuenta1=CuentaBancaria("Carlos", 100000)
cuenta2=CuentaBancaria("Ana", 50000)

cuenta1.depositar(50000)
cuenta1.retirar(30000)
cuenta2.retirar(60000)
print(cuenta1.mostrar_datos())
print(cuenta2.mostrar_datos())