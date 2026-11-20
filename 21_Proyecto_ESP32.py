from machine import Pin, time_pulse_us
from time import sleep, sleep_us
import sys
import select

# Configuración de pines ORIGINAL
trig = Pin(18, Pin.OUT)
echo = Pin(19, Pin.IN)
led_rojo = Pin(25, Pin.OUT)   # Rojo vuelve al 25
led_verde = Pin(26, Pin.OUT)  # Verde vuelve al 26

# Apagar LEDs al inicio
led_rojo.value(0)
led_verde.value(0)

estado_actual = "NORMAL"
estado_parpadeo = False 

while True:
    # 1. Leer distancia
    trig.value(0)
    sleep_us(2)
    trig.value(1)
    sleep_us(10)
    trig.value(0)
    
    tiempo = time_pulse_us(echo, 1, 30000)
    if tiempo > 0:
        distancia = tiempo / 58
        print(round(distancia, 1))
        
    # 2. Leer comando de la PC
    if select.select([sys.stdin], [], [], 0.0)[0]:
        mensaje = sys.stdin.readline().strip()
        
        if "ALERTA" in mensaje:
            estado_actual = "ALERTA"
        elif "PRECAUCION" in mensaje:
            estado_actual = "PRECAUCION"
        elif "NORMAL" in mensaje:
            estado_actual = "NORMAL"
            
    # 3. Lógica de LEDs
    if estado_actual == "ALERTA":
        # 0 a 10 cm: Rojo encendido, Verde APAGADO
        led_rojo.value(1)
        led_verde.value(0)
        
    elif estado_actual == "PRECAUCION":
        # 10 a 20 cm: Rojo parpadeando, Verde APAGADO
        led_verde.value(0)  
        
        estado_parpadeo = not estado_parpadeo
        if estado_parpadeo:
            led_rojo.value(0)
        else:
            led_rojo.value(0)
            
    elif estado_actual == "NORMAL":
        # Más de 20 cm: Verde encendido, Rojo APAGADO
        led_rojo.value(0)   
        led_verde.value(1)
            
    sleep(0.2)