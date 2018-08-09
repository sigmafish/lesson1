from gpiozero import RGBLED
from time import sleep

if __name__ == '__main__':
    # initialize the gpio pin
    rgbled = RGBLED(12, 20, 21) #(r,g,b)
    rgb_color = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (0,0,0)]
    
    i=0
    mode=3
    
    while(i<10):
##        print(i)
        rgbled.color=rgb_color[i%mode]
        sleep(1)
        i += 1
    
    # turn off led
    rgbled.color=rgb_color[mode]
    