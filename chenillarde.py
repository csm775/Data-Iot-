from machine import Pin # importe dans le code la lib qui permet de gerer les Pins de sortie
import utime # importe dans le code la lib qui permet de gerer le temps

pinNumber = 12 # declaration d'une variable pinNumber à 17
led = Pin(pinNumber, mode=Pin.OUT)

pinNumber = 13 # declaration d'une variable pinNumber à 17
led1 = Pin(pinNumber, mode=Pin.OUT)

pinNumber = 14 # declaration d'une variable pinNumber à 17
led2 = Pin(pinNumber, mode=Pin.OUT)

while True:          # boucle infini
    led.toggle()
    utime.sleep(1)
    led.on()
    led.off()

    led1.toggle()
    utime.sleep(1)
    led1.on()
    led1.off()

    led2.toggle()
    utime.sleep(1)
    led2.on()
    led2.off()