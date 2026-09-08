# # contador = 1

# # while contador <= 5:
# #     print(contador)
# #     contador += 1

# # for numero in range(1, 6):
# #     print(numero)

# # range(): El final no se incluye

# for numero in range(2, 7):
#     print(numero)

#range(5)
# 0, 1, 2, 3, 4

#range(1, 6)
# 1, 2, 3, 5

#range(0, 11, 2)
#0, 2, 4, 6, 8, 10

#for numero in range(10, 1, -2):
    #print(numero)



# FOR COMO CONTADOR
# total = 0

# for vuelta in range(4):
#     numero = int(input("Numero: "))
#     total = total + numero
# print ("Total: ", total)


# FOR + IF DECIDIR EN CADA REPETICION

# for numero in range(1, 11):
#     if numero % 2 == 0:
#         print(numero, "es par")
#     else:
#         print(numero, "es impar")

# CONTADOR Y ACUMULADOR DENTRO DEL FOR
# contador = 0
# suma = 0

# for numero in range(1, 11):
#     if numero % 2 == 0:
#         contador += 1
#         suma += numero
# print ("Cantidad de pares:, ", contador)
# print("Suma de pares: ", suma)

# BREAK Y CONTINUE  FUNCIONANDO CON FOR

# for numero in range(1, 8):
#     if numero == 4:
#     break
# print(numero)


# for numero in range(1, 8):
#      if numero == 4:
#          continue
# print(numero)


# FOR TAMBIEN RECCORE ERRORES
# texto = "Hola"
# for letra in texto:
#     print("Letra", letra)

# texto = "AREA TECNICA"
# texto = texto.lower() # lower ayuda a comparar sin preocuparse por mayuscula
# if texto in "aeiouáéíóú":
#     ...

#   LEN(), INDICES Y SLICING LEN SIRVE PARA IMPRIMIR CARACTERES 
# texto = "Python"
# len (texto) #6
# texto[0] #p
# print(texto, 0)
# texto[-1] #n
# texto[0:3] #Pyt
# texto[::-1] #nohtyp

# # LISTAS GUARDAR VARIOS VALORES: La lista agrupa varios elemetos en una sola variable
# notas = [4.5, 3.8, 5.0, 2.9]
# print(notas[0]) 
# print(notas[-1])
# print(len(notas))  
# len(lista) devuelve la cantidad de elementos


# RECORRER LISTAS CON FOR: La variable for toma lelemntos de la lista 
# notas = [4.5, 3.0, 5.0]
# for nota in notas:
#     print("Notas: ", nota)
    
# suma = 0 
# for nota in notas: 
#     suma += nota
# promedio = suma / len(notas)
# print("Promedio: ", promedio)

# APPEND: Construir una lista con datos del usuario, agrega un elemento al final de la lista 
# notas = []
# for vuelta in range(3):
#     nota = float(input("Ingrese una nota: "))
#     notas.append(nota)
# print(notas)
# append() no reemplaza: agrega al final 

# MODIFICA ELEMENTOS DENTRO DE UNA LISTA: Cada operacion cambia la lista de una manera distinta
# frutas = ["Manzana", "Pera", "Uva"]
# frutas[1] = "Mango"
# frutas.remove ("Uva")
# eliminada = frutas.pop(0)
# print(frutas)
# print(eliminada)

# HERRAMIENTAS UTILES EN LISTA
# numeros = [30,10,40,20]
# index = numeros.index(40)
# count = numeros.count(50)
# # numeros.sort() # Modifica la lista
# # ordenada = sorted(numeros) # crea otra lista
# # numeros.reverse() # Invierte el orden actual
# #numeros.count(20) # cuenta coicidencias
# numeros.index(40) # Primera posicion donde
# print(numeros)


# CUANDO NECESITO LA POSICION: range(len(lista))

# nombres =["Ana", "Luis", "Carlos"]
# for i in range(len(nombres)):
#     print("Estudiantes", i + 1, ":", nombres[i])

# notas = [2.5, 3.0, 4.0, 1.8]
# for i in range(len(notas)):
#     if notas[i] <3.0:
#         notas[i] = 3.0
# print(notas)
# con indices puede hacer: lista[i] = nuevo_valor

# LISTAS ANIDADAS: LISTAS DENTRO DE LISTAS: Sirven para representar datos con varias columnas 
# estudiantes = [
#     ["Ana", 4.5],
#     ["Luis", 3.8],
#     ["Carlos, 4.2"],
# ]
# #print (estudiantes[2][1])
# for estudiante in estudiantes:
#     print(estudiantes[0], estudiantes[1])


# PROMEDIO CON LISTAS ANIDADAS El acululador debe reiniciarse para cada estudiantes
estudiantes =[
    ["Ana", [4.0, 3.5, 5.0]],
    ["Luis", [2.8, 3.0, 4.2]]
]
for estudiante in estudiantes: 
    suma = 0 
    for nota in estudiante[1]:
        suma += nota 
    promedio = suma / len(estudiante[1])
    print(estudiante[0], round(promedio, 2))
    