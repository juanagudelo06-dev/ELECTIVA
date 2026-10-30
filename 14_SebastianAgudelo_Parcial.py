# productos=[]

# with open("productos.txt","w") as archivo: 
#      for i in range(3):
#         nombre=input("Nombre del producto: ")
#         cantidad=int(input("Digite la cantidad de productos: "))
#         precio=float(input("Digite el valor unitario: "))
#         producto={
#             "nombre":nombre,
#             "cantidad":cantidad,
#             "precio":precio
#         }
#         productos.append(producto)
#         archivo.write(producto["nombre"] + "," + str(producto["cantidad"]) + "," + str(producto["precio"]) + "\n" )
       
# totaltodos=0
# totalindividual=0
# with open("productos.txt", "r") as archivo:
#      for linea in archivo:
#             datos  = linea.strip().split(",")
#             nombre=datos[0]
#             cantidad=int(datos[1])
#             precio=float(datos[2])

#             total=cantidad*precio 
#             totaltodos+=total
# print("El total de todo es: ", totaltodos)        
 
#Segundo punnto:

class Dispositivo:
    def __init__(self, nombre, marca, precio):
        self.nombre=nombre
        self.marca=marca
        self.precio=precio
    
    def mostrar(self):
         return f"Nombre: {self.nombre} Marca: {self.marca} Precio: {self.precio}"
    def calcular_descuento(self, porcentaje):
        descuento= self.precio*porcentaje
        precio_final=self.precio-descuento
        return precio_final
class Sensor(Dispositivo):
    def __init__(self, nombre, marca, precio, unidad,estado):
        super().__init__(nombre, marca, precio)
        self.__estado=estado
        self.unidad=unidad
    def mostrar_estado(self, nuevo_esatdo):
        if nuevo_esatdo=="Activo":
            self.__estado="Activo"
        else:
            self.__estado="Inactivo"
    def mostrar(self):
         return f"Nombre: {self.nombre} Marca: {self.marca} Precio: {self.precio} Unidad: {self.unidad} Estado: {self.__estado}"    
    def sen_limite(self, limite):
        if limite>80:
            print(f"Ha alcanado el limite de la temperatura")
        else:
    
            print(f"La temperatura aun esta en optimas condiciones{self.limite}")

sensor1=Sensor("Caixun 12P", "caixun", 125000, "grados", "Activo")
sensor2=Sensor("Neutro 39N", "chichi", 210000, "grados", "Inactivo")   

print(sensor1.mostrar())
# print(sensor1.sen_limite)
print("\n" + sensor2.mostrar())
# print(sensor1.sen_limite)

sensor1.mostrar_estadoestado("Inactivo")
print(f"El nuevo estado del sensor 1 es: {sensor1.estado()}")

porcentaje_descuento = 0.15 
precio_rebajado = sensor1.calcular_descuento(porcentaje_descuento)
print(f"El precio original del {sensor1.nombre} es ${sensor1.precio:,.2f}")
print(f"Con un descuento del 15%, el precio final es ${precio_rebajado:,.2f}")  

