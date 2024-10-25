#Firmware V0.1
#Codigo Escrito por Victor Lau 24/10/2024
# Codigo de Prueba para encender y apagar Reles del SMARC MK1
from machine import Pin
import time

# Definir cada relé con una variable independiente
relay_1 = Pin(25, Pin.OUT)
relay_2 = Pin(33, Pin.OUT)
relay_3 = Pin(32, Pin.OUT)
relay_4 = Pin(26, Pin.OUT)

# Función para encender los relés con 2 segundos de diferencia
def start():
    relay_1.value(1)
    relay_2.value(1)
    relay_3.value(1)
    relay_4.value(1)
    
def turn_on_relays():
    relay_1.value(0)
    time.sleep(2)
    relay_2.value(0)
    time.sleep(2)
    relay_3.value(0)
    time.sleep(2)
    relay_4.value(0)

# Función para apagar los relés en el mismo orden
def turn_off_relays():
    relay_1.value(1)
    time.sleep(2)
    relay_2.value(1)
    time.sleep(2)
    relay_3.value(1)
    time.sleep(2)
    relay_4.value(1)

# Bucle principal
while True:
    start()
    turn_on_relays()    # Encender los relés uno por uno
    time.sleep(2)       # Esperar 2 segundos después de que todos se enciendan
    turn_off_relays()   # Apagar los relés uno por uno
    time.sleep(5)       # Esperar 5 segundos antes de repetir

