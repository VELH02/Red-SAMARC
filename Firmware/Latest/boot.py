import network
import urequests
import machine
import os
from machine import Pin
import time

# Configuración de red WiFi
ssid = "DCI-Lab"
password = "DCI-Lab2024"

# Configuración de la URL del archivo de actualización en GitHub
github_url = "https://raw.githubusercontent.com/VELH02/SMARC-Network/refs/heads/main/Firmware/Latest/Firmware.py"  # Cambia esta URL según tu archivo

# Función para conectarse a la red WiFi
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        pass
    print("Conectado a WiFi:", wlan.ifconfig())

# Función para descargar el archivo de actualización
def download_update():
    try:
        print("Descargando actualización desde GitHub...")
        response = urequests.get(github_url)
        if response.status_code == 200:
            with open("main.py", "w") as f:
                f.write(response.text)
            print("Actualización completada.")
        else:
            print("No se pudo descargar el archivo, código de estado:", response.status_code)
        response.close()
    except Exception as e:
        print("Error al descargar la actualización:", e)

# Función para ejecutar el archivo descargado
def run_main():
    try:
        with open("main.py") as f:
            code = f.read()  # Leer el contenido de main.py
            exec(code)       # Ejecutar el contenido de main.py
        print("main.py ejecutado exitosamente.")
    except OSError:
        print("No se encontró el archivo main.py.")
    except Exception as e:
        print("Error al ejecutar main.py:", e)

# Secuencia de inicio
connect_to_wifi()     # Conectar a la red WiFi
download_update()     # Descargar la última versión de main.py desde GitHub
run_main()            # Ejecutar el archivo descargado
