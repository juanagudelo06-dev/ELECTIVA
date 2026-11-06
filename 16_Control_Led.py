from machine import Pin
import sys

led=Pin(18, Pin.OUT)

while True:
    mensaje=sys.stdin.readline().strip()
    
    if mensaje =="ENCENDER":
        led.value(1)
        
    if mensaje =="APAGAR":
        led.value(0)
        
#python -mmpremote connect com"puerto como tal" run nombre del arhivo
#python -m mpremote connect COM12 fs ls 16_Cntrol_Led.py :main.py