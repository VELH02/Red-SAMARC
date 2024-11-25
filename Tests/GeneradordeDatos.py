import random
import csv
import datetime
import time

# Abrir un archivo CSV para escribir los datos
with open('datos.csv', mode='w', newline='') as archivo_datos:
    escritor_datos = csv.writer(archivo_datos)
    # Escribir el encabezado
    escritor_datos.writerow(['Tiempo', 'Temperatura', 'Humedad', 'PM2.5', 'PM10', 'Vsolar', 'Isolar', 'VBat', 'IBat'])
    
    try:
        while True:
            # Obtener el tiempo actual
            tiempo = datetime.datetime.now()
            tiempo_str = tiempo.strftime('%Y-%m-%d %H:%M:%S')
            
            # Generar datos aleatorios
            temperatura = round(random.uniform(15, 35), 2)
            print("Temp: ", temperatura, "°C")
            humedad = round(random.uniform(20, 80), 2)
            print(humedad)
            pm25 = round(random.uniform(0, 100), 2)
            print(pm25)
            pm10 = round(random.uniform(0, 150), 2)
            print(pm10)
            vsolar = round(random.uniform(0, 20), 2)
            print(vsolar)
            isolar = round(random.uniform(0, 5), 2)
            print(isolar)
            vbat = round(random.uniform(10, 14), 2)
            print(vbat)
            ibat = round(random.uniform(-5, 5), 2)
            print(ibat)
            
            # Escribir los datos en el CSV
            escritor_datos.writerow([tiempo_str, temperatura, humedad, pm25, pm10, vsolar, isolar, vbat, ibat])
            archivo_datos.flush()  # Asegurar que los datos se escriben en el archivo
            
            # Esperar un minuto antes de generar el siguiente dato
            time.sleep(60)
    except KeyboardInterrupt:
        print("Programa detenido por el usuario.")
