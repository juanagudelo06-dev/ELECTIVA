import serial
from time import sleep

# Configura el puerto serial (Asegúrate de que sea COM3 o el que estés usando)
puerto = serial.Serial("COM3", 115200, timeout=3)
sleep(3) # Da tiempo a que se establezca la conexión

puerto.reset_input_buffer() # Limpia basura del puerto

while True:
    # Leer la distancia enviada por la ESP32
    dato = puerto.readline().decode('utf-8').strip()
    
    try: 
        distancia = float(dato)
        
        # Lógica del proyecto final
        if distancia <= 10:
            print(f"Distancia: {distancia} cm - [¡ALERTA!] Objeto demasiado cerca.")
            puerto.write(b'ALERTA\n') # Ordena encender el LED Rojo
            
        elif distancia > 10 and distancia <= 20:
            print(f"Distancia: {distancia} cm - [PRECAUCIÓN] Objeto aproximándose.")
            puerto.write(b'PRECAUCION\n') # Ordena parpadear el LED Rojo
            
        elif distancia > 20:
            print(f"Distancia: {distancia} cm - [NORMALIDAD] Vía libre.")
            puerto.write(b'NORMAL\n') # Ordena encender el LED Verde
            
    except ValueError:
        # Ignora si llega un dato vacío o corrupto por el cable
        pass