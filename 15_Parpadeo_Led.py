# Velocidad de comunicacion
# Los extremos deben utilizar la misma velocidad de comunicacion

# Esp32 = 115200

# Que es el py serial
# Es la libreria que permite a ýthon utilizar eñl puerto serial del computador
# import serial

# Abrir el puerto desde python 

# import serial
# puerto = serial.Serial("COM10", 115200)

# puerto.write()#solo envia y la placa toma la decisiòn
# puerto serial envia bytes y necesitamos convertirlo a texto
# encode()
# puerto.write((mensaje + "\n").encode())
# el salto de linea determina en que parte termina el mensaje
# El receptor puede leer un mensaje completo con 
# readline()

# Para recibir informaciòn de la ESP al pc readline()

# dato=puerto.readline()

# decode para recibir bytes y convertir a texto para enviar de esp a pc

# dato=puerto.readline().decode()

# dato=puerto.readline().decode().strip() 
# temperatura = float(dato)


#python -m mpremote run nombre del archivo.py
from machine import Pin
from time import sleep

led=Pin(18, Pin.OUT)

while True:
    led.value(1)
    sleep(1)
    
    led.value(0)
    sleep(1)

