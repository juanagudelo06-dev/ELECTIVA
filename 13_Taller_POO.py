#  Indicaciones generales
# • Desarrolle los ejercicios utilizando los conceptos trabajados durante la Unidad 3 y sus apuntes de
# clase.
# • Pruebe el programa durante su construcción y revise los mensajes de error antes de solicitar
# ayuda.
# • Verifique los tipos de datos, la indentación, la lectura y escritura de archivos y el comportamiento
# de los objetos creados.
# • El programa debe cumplir todos los requerimientos del enunciado, no basta con que se ejecute
# sin errores.
# Ejercicio 1. Registro y consulta de equipos tecnológicos
# Una empresa necesita llevar un registro básico de los equipos tecnológicos disponibles. Desarrolle un
# programa en Python que permita registrar cuatro equipos. De cada equipo se debe solicitar el nombre,
# la cantidad disponible y el valor unitario.
# 1. Registrar cuatro equipos y almacenar la información de forma organizada durante la ejecución del
# programa.
# 2. Crear desde el programa un archivo llamado equipos.txt y guardar cada equipo en una línea con el
# formato: nombre,cantidad,valor_unitario
# 3. Después de guardar la información, volver a abrir y leer el archivo para procesar los datos
# registrados.
# 4. Convertir los datos numéricos recuperados del archivo al tipo correspondiente antes de realizar
# operaciones con ellos.
# 5. Calcular y mostrar el valor total de cada equipo, teniendo en cuenta que valor total = cantidad × valor
# unitario.
# 6. Mostrar únicamente los equipos cuyo valor total sea superior a $2.000.000
# 7. Calcular y mostrar el valor total de todos los equipos registrados.
# # Ejemplo del formato esperado en el archivo: Portatil,4,2500000

# equipos = []
# with open("equipos.txt", "w") as archivo: 
#     for i in range(4):
#         print(f"Registro del equipo {i+1}")
#         nombre = input("Nombre del equipo: ")
#         cantidad = int(input("Cantidad disponible: "))
#         valor_unitario = float(input("Valor unitario: "))
        
#         archivo.write(f"{nombre},{cantidad},{valor_unitario}\n")

# gran_total = 0
# equipos_mayores_2m = []

# print("\n Valor total de cada equipo")

# with open("equipos.txt", "r") as archivo:
#     for linea in archivo:
#         datos = linea.strip().split(",")
#         nombre = datos[0]
#         cantidad = int(datos[1])
#         valor_unitario = float(datos[2])
        
#         valor_total = cantidad * valor_unitario
#         gran_total += valor_total
       
#         print(f"{nombre}: ${valor_total:,.2f}")
        
#         if valor_total > 2000000:
#             equipos_mayores_2m.append((nombre, valor_total))

# print("\nEquipos con valor total superior a $2.000.000")
# for nombre, valor in equipos_mayores_2m:
#     print(f"{nombre}: ${valor:,.2f}")

# print(f"\nValor total de todos los equipos registrados: ${gran_total:,.2f}")

# Ejercicio 2. Sistema de dispositivos con Programación Orientada a Objetos 
# Una empresa desea representar diferentes dispositivos tecnológicos mediante POO. Desarrolle un 
# programa que cumpla los siguientes requerimientos. 
# 1.  Crear una clase Dispositivo con los atributos nombre, marca y precio. 
# 2.  La clase Dispositivo debe permitir mostrar la información del dispositivo y calcular su precio 
# después de aplicar un porcentaje de descuento. El porcentaje puede expresarse en formato 
# decimal; por ejemplo, 0.10 representa un 10 %. 
# 3.  Crear una clase Computador que herede de Dispositivo e incorpore los atributos memoria_ram y 
# estado. 
# 4.  El atributo estado debe estar encapsulado y su modificación debe realizarse mediante un método 
# que solo acepte los valores "Disponible" o "Prestado". 
# 5.  La clase Computador debe permitir consultar el estado actual, mostrar toda la información del 
# computador y determinar si posee 16 GB de memoria RAM o más. 
# 6.  Crear al menos dos objetos de tipo Computador y mostrar la información de ambos. 
# 7.  Cambiar el estado de uno de los computadores y comprobar su nuevo estado. 
# 8.  Intentar asignar un estado diferente de "Disponible" o "Prestado" y verificar que el cambio no se 
# realice. 
# 9.  Aplicar un descuento a uno de los computadores y mostrar el valor obtenido. 
# Revisión antes de finalizar 
# • Ejecute cada programa con datos de prueba y compruebe que los resultados sean coherentes. 
# • Revise que el archivo generado contenga los registros esperados y que pueda ser leído 
# nuevamente por el programa. 
# • Compruebe que los métodos de las clases funcionen sobre los objetos creados y que la validación 
# del estado se cumpla.

class Dispositivo:
    def __init__(self, nombre, marca, precio):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio 
    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}  Marca: {self.marca}  Precio: ${self.precio:,.2f}"
    def calcular_descuento(self, porcentaje):
        descuento = self.precio * porcentaje
        precio_final = self.precio - descuento
        return precio_final
class Computador(Dispositivo):
    def __init__(self, nombre, marca, precio, memoria_ram, estado_inicial):
        super().__init__(nombre, marca, precio)
        self.memoria_ram = memoria_ram
        self.__estado = "Disponible" 
        self.cambiar_estado(estado_inicial) 
    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado == "Disponible" or nuevo_estado == "Prestado":
            self.__estado = nuevo_estado
        else:
            print(f"Error: '{nuevo_estado}' es un estado inválido. Solo se acepta 'Disponible' o 'Prestado'.")    
    def consultar_estado(self):
        return self.__estado
    def mostrar_info_computador(self):
        info_basica = super().mostrar_informacion()
        return f"{info_basica} | RAM: {self.memoria_ram}GB | Estado: {self.__estado}"
    def verificar_ram(self):
        if self.memoria_ram >= 16:
            return f"El equipo {self.nombre} es óptimo (Tiene {self.memoria_ram}GB de RAM)."
        else:
            return f"El equipo {self.nombre} tiene capacidad básica (Tiene {self.memoria_ram}GB de RAM)."

#Pruebas 
print("Creación y muestra de información de los objetos ")
compu1 = Computador("Aspire 17", "Acer", 3500000, 16, "Disponible")
compu2 = Computador("HP G10", "Hewlett-Packard", 2200000, 8, "Prestado")

print(compu1.mostrar_info_computador())
print(compu1.verificar_ram())
print("\n" + compu2.mostrar_info_computador())
print(compu2.verificar_ram())

print("\n Cambiar estado de uno de los computadores")
compu1.cambiar_estado("Prestado")
print(f"El nuevo estado de {compu1.nombre} es: {compu1.consultar_estado()}")

print("\n Intentar asignar un estado inválido")
compu2.cambiar_estado("En reparación")
print(f"El estado de {compu2.nombre} se mantiene seguro como: {compu2.consultar_estado()}")

print("\n Aplicar un descuento")
porcentaje_descuento = 0.15 
precio_rebajado = compu1.calcular_descuento(porcentaje_descuento)
print(f"El precio original del {compu1.nombre} es ${compu1.precio:,.2f}")
print(f"Con un descuento del 15%, el precio final es ${precio_rebajado:,.2f}")
    

    