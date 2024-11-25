from sds011lib import SDS011QueryReader
from serial import Serial
import time

# Setup a query-mode reader on /dev/ttyUSB0 
sensor = SDS011QueryReader('COM4')

# Read some data!

while True:
    aqi = sensor.query()
    print("PM2.5= ", aqi.pm25)
    print("PM10= ", aqi.pm10)
    time.sleep(1)
