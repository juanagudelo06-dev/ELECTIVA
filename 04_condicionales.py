# edad= int(input("digite su edad por favor "))
# if edad>=18:
#    print("Puede ingresar")

# edad= int(input("digite su edad por favor "))
# if edad>=18:
#    print("Mayor de edad")
# else:
#    print("Menor de edad")

# nota= float(input("digite su nota por favor "))
# if nota>=3:
#    print("Aprobado")
# else:
#    print("No Aprobado")

# nota= float(input("digite su nota por favor "))
# if nota<3:
#    print("Insuficiente")
# elif nota<4:
#    print("Basico")
# elif nota<4.6:
#    print("Alto")
# else :
#    print("Superior")

# nota= float(input("digite su nota por favor "))
# if nota>=3 and nota<4.5:
#    print("Aprobado")
# elif nota>=4.5:
#    print("Excelente")

# nota= float(input("digite su nota por favor "))
# if nota<0 or nota>5:
#    print("Nota no valida")
# elif nota<3:
#    print("Insuficiente")
# elif nota<4:
#    print("Basico")
# elif nota<4.6:
#    print("Alto")
# else :
#    print("Superior")

# 2 DIA DE CONDICIONALES 




#  usuario= input("usuario: ")   
#  nombre =input("nombre: ")
#  edad= input("edad: ")
#  temperaturacorporal=float(input("temperaturacorporal: "))
#  nota=float(input("NOTA DE 0.0 A 5.0 "))
#  carnet = input ("¿tiene carnet? si o no : ")

#  mayor_edad=edad>=18
#  temp_adecuada=temperaturacorporal==37.5
#  notafinal=nota>=0.0 and nota<=5.0
#  requisito=carnet=="si"
#  cumple_requisitos=mayor_edad and temp_adecuada and requisito

#  print ("cumple requisitos de ingreso ",    cumple_requisitos)
#  print ("es mayor de edad",   mayor_edad)
#  print("tiene carnet" ,requisito)
#  print("tiene temperatura normal",temp_adecuada )


# nota=float(input("Nota: "))
# if nota<0 or nota >5:
#   print("nota no valida")
# elif nota <3
#      print (insufuciente)
# elif nota<4.6:
#      print (alto)


# edad = 25
# matricula = "si"
# contraseña = "azul21"

# if edad < 18:
#     print("Acceso retringido")
# else :
#     if matricula == "si" :
#         if contraseña =="azul21" :
#              print("Bienvenido")
#         else:
#              print("Contraseña incorrecta ")    
#     else:
#          print("No matriculado")   

# nombre =input("nombre: ")
# edad=  int(input("edad: "))
# invitacion = input ("¿tiene invitacion ? si o no:")
# invitacion = invitacion.lower()
# if edad >= 18 and invitacion == "si" :
#     print("Autorizado ", nombre)
# elif edad>=18 and invitacion== "no":
#      print("Necesita invitacion ", nombre)
# else:          
#      print("Acceso retringido", nombre)

# numero = 1
# while numero <=5:
#     print(numero)
#     numero=numero + 1

# contador = 1
# while contador <=3:
#     print(contador)
#     contador = contador + 1


# numero = 1
# while numero <=3:
#     print(numero)

contraseña = ""
intentos = 0

while contraseña != "python" and intentos < 3:
     contraseña = input("contraseña: ")
     intentos = intentos + 1

if contraseña =="python":
  print ("Acceso autorizado")     
else:
  print ("Acceso bloqueado")

  pin_correcto = ""
intentos = 0


while intentos < 3 and pin_correcto != "2580":
     pin_ingreso= input("pin_correcto: ")
     intentos = intentos + 1 
if pin_correcto =="2580":
     print ("Acceso a la cuenta ")   
else:
     print ("tarjeta bloqueada")