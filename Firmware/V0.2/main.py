from machine import Pin, UART
import time
import sds011
import dht
import random
import utime  # Utilizamos utime en lugar de time

# Definir cada relé con una variable independiente
relay_1 = Pin(25, Pin.OUT)
relay_2 = Pin(33, Pin.OUT)
relay_3 = Pin(32, Pin.OUT)
relay_4 = Pin(26, Pin.OUT)

d = dht.DHT22(machine.Pin(19))
uart = UART(1, baudrate = 9600, rx = 16, tx = 17)
dust_sensor = sds011.SDS011(uart)

# Nombre del archivo CSV
archivo_csv = 'datos_sensores.csv'  # Ruta donde se almacenarán los datos

# Función para inicializar el archivo CSV con los encabezados
def inicializar_csv():
    try:
        with open(archivo_csv, 'w') as file:  # Abrir en modo de escritura para agregar encabezados
            file.write('Fecha,Temperatura (°C),Humedad (%),Presión (hPa),PM2.5 (µg/m³),PM10 (µg/m³)\n')
    except OSError as e:
        print("Error al crear el archivo CSV:", e)

# Función para guardar los datos en el CSV
def guardar_datos(tr, h, p, pm25, pm10):
    # Obtener la fecha y hora actual, Por alguna razon estamos en francia
    timestamp = utime.localtime()
    fecha_hora = f'{timestamp[0]}-{timestamp[1]:02d}-{timestamp[2]:02d} {timestamp[3]:02d}:{timestamp[4]:02d}:{timestamp[5]:02d}'
    
    # Guardar los datos en el archivo CSV
    with open(archivo_csv, 'a') as file:
        file.write(f'{fecha_hora},{tr},{h},{p},{pm25},{pm10}\n')

# Función para enviar datos NO SIRVEEE
def enviar_datos():
    aio.send("temperatura", tr)
    aio.send("presion", p)
    aio.send("humedad", h)
    aio.send("particulas-pm2-dot-5", pm25)
    aio.send("particulas-pm10", pm10)

# Inicializamos el archivo CSV si no existe
inicializar_csv()

# Bucle principal
while True:
    d.measure()  # Medir la temperatura y humedad
    tr = d.temperature()
    h = d.humidity()
    p = 1003  # Presión simulada
    
    dust_sensor.wake()  # Despertamos el sensor de polvo
    dust_sensor.read()  # Leemos los valores de PM2.5 y PM10
    pm25 = dust_sensor.pm25
    pm10 = dust_sensor.pm10
    
    # Imprimimos los valores obtenidos
    print(f'Temp: {tr} °C')
    print(f'Humidity: {h} %')
    print(f'PM2.5: {pm25} µg/m³')
    print(f'PM10: {pm10} µg/m³')
    
    # Guardamos los datos en el archivo CSV
    guardar_datos(tr, h, p, pm25, pm10)
    print("Datos guardados")
    
    # enviar_datos()  # nO SIRVE
    
    time.sleep(5)  # Esperar un minuto antes de la siguiente lectura
