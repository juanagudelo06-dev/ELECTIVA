import serial
from time import sleep

puerto = serial.Serial("COM10",115200)

sleep(3)

puerto.reset_input_buffer()

while True:
    mensaje = input("Digite ENCENDER o APAGAR: ")
    puerto.write((mensaje + "\n"))