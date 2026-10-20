#HERENCIA Y ENCAPSULAMIENTO 

#Pass Permite ejecutar sin necesidad de tener codigo dentro de esa clase

# class Persona:
#     def __init__(self,nombre):
#         self.nombre = nombre
        
#     def saludar(self):
#         return f"Hola, soy{self.nombre}"

# class Estudiante(Persona):# En esta clase la clase padre debe estar en parentesis
#     estudiante1 = Estudiante("Pepito")
#     print(estudiante1.saludar())
# pass

#Persona tiene constructor y tiene el metodo saludar()
# Estudiante no agrega nada nuevo, Pero Hereda lo de la persona. 
# Para que sirve super()

#super() permite ejecutar el constructor o los metodos de la clase padre 

# class Persona:
#     def __init__(self,nombre, edad):
#         self.nombre = nombre
#         self.edad = edad
        
# class Estudiante(Persona):
#     def __init__(self, nombre, edad, carrera):
#         super().__init__(nombre, edad)
#         self.carrera=carrera
        
# class Estudiante(Persona):
#     def __init__(self, nombre, edad, carrera, nota):
#         super().__init__(nombre, edad)
#         self.carrera=carrera
#         self.__nota=nota
        
# estudainte1=Estudiante("Luis", 34, "Lic. Tecnologia", 4.5)
#podemos heredar metodos y clases

# estudiante1.presentarse()
# #metodo heredado de persona

# estudiante1.mostrar_nota()
# #Metoo propio de Estudiante

# estudiante1.obtener_estado()
# #Metodo propio de Estudiante

#sobrescritura de metodos
# class Persona:
#     def presentarse(self):
#         return "soy una persona"
    
# class Estudiante(Persona):
#     def presentarse(self):
#         return "Soy un estudiante"
    
# class Estudiante:
#     def __init__(self, nota):
#         self.__nota=nota
        
#     def mostra_nota(self):
#         return self.__nota #Acesso controlado (Privado) con __ solo se puede modificar dentro de la clase
#lo anterior pertenece a el encapsulamiento
    
#__atributo y __atributo acceso restringido
#_atributo Uso interno por convenciòn

# class Sensor:
#     def __init__(self):
#         self._ubicaciòn="Sala"
#         self.__temperatura=25
#_ubicaciòn es interno por convenciòn
#__temperatura es controla desde mètodos

#Getter y setter son metodos
#Getter leer o consultar un dato 
#Setter nos permite modifiar un dato

# class Estudiante:
#     def __init__(self, nota):
#         self.__nota=nota
#     def mostrar_nota(self):
#         return self.__nota
#     def cambiar_nota(self, nueva_nota):
#         if 0<=nueva_nota<=5:
#             self.__nota=nueva_nota
#     def obtener_estado(self):
#         if self.__nota>=3:
#             return f"Aprobado con: {self.__nota}"
#         else:
#             return f"Reprobado con: {self.__nota}"
#  #Metodo obtener estado       
        
# estudiante1=Estudiante(4.5)
# print(estudiante1.mostrar_nota())

# estudiante1.cambiar_nota(3.8)
# print(estudiante1.mostrar_nota())

# estudiante1.cambiar_nota(7)
# print(estudiante1.mostrar_nota())    

# print(estudiante1.obtener_estado())

#Dos objetos, estados diferentes ambos son estudiante pero cada uno onseva su propia informaciòn

# estudiante1=Estudiante("Luis", 34, "Lic. Tecnologia",4.5)
# estudiante2=Estudiante("Pedro", 25, "Lic. Tecnologia",2.8)

# print(estudiante1.obtener_estado())
# print(estudiante2.obtener_estado())

#Encapsular los datos que no deberian modificarse libremente desde cualquier parte del programa
# class Cuenta:
#     def __init__(self, titular, saldo):
#         self.titular=titular
#         self.__saldo=saldo
        
#     def consultar_saldo(self):
#         return self.__saldo
#     def depositar(self, cantidad):
#         if cantidad>0:
#             self.__saldo+=cantidad

#actividad: construye el sistema Persona Estudiante y pruea dos objetos

class Persona:
    def __init__(self, nombre,edad):
        self.nombre=nombre
        self.edad=edad
        
    def presentarse(self):
        return f"Bienvenido {self.edad}, {self.nombre}"
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera, nota):
        super().__init__(nombre, edad)
        self.carrera=carrera
        self.__nota=nota
        
    def mostrar_nota(self):
        return self.__nota
    
    def cambiar_nota(self, nueva_nota):
        if 0<=nueva_nota<=5:
            self.__nota=nueva_nota
    
    def obtener_estado(self):
        if self.__nota>=3:
           return f"Aprobado con: {self.__nota}"
        else:
            return f"Reprobado con: {self.__nota}"
        
estudiante1=Estudiante("Carlitos", 22,"Lic. Tecnologia", 3.5)
estudiante2=Estudiante("Pedro", 25, "Lic. Tecnologia",2.8)

print(estudiante1.mostrar_nota())
print(estudiante1.obtener_estado())
estudiante1.cambiar_nota(6)
print(estudiante1.obtener_estado())
print(estudiante2.mostrar_nota())
print(estudiante2.obtener_estado())