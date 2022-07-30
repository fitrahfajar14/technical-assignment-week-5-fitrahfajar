import RPi.GPIO
import time
import dht11

RPi.GPIO.setmode(RPi.GPIO.BCM)

sensor = dht11.DHT11(pin = 4)

while True:
    result = dht11.read_retry(sensor, pin)
    print("Temperature: %d C" % result.temperature)
    print("Humidity: %d %%" % result.humidity)
else :
    print("gagal membaca")
    time.sleep(3)
        