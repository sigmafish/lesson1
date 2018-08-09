from gpiozero import LED, PWMLED
##from gpiozero import PWMLED
from signal import pause
from time import sleep
# unit of sleep: 1 sec 

# initialize the gpio pin
green = LED(20)
red = PWMLED(21)

green.blink()

while True:
    red.value = 0  # off
    sleep(1)
    red.value = 0.3  # half brightness
    sleep(1)
    red.value = 1  # full brightness
    sleep(1)
    
pause()    