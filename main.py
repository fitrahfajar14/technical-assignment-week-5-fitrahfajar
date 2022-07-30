import RPi.GPIO
import time
import dht11

RPi.GPIO.setmode(RPi.GPIO.BCM)

sensor = dht11.DHT11(pin = 4)
  
while True:
    result = dht11.read_retry(sensor, pin)
    print("Temperature: %d C" % result.temperature)
    print("Humidity: %d %%" % result.humidity)

        #Logic tambahan :
        if temp > 30 :
            print("suhu terasa panas")
        elif temp <= 30 and temp >= 24 :
            print("suhu terasa sejuk")
        else :
            print("suhu terasa dingin")
            
    else :
        print("Gagal Membaca")
    time.sleep(3)