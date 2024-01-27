from machine import Pin,PWM
import time
led13 = PWM(Pin(13))

led13.freq(1000)
def main():
    while True:
        for i in range(0 , 1023):
            led13.duty(i)
            time.sleep_ms(2)
        for i in range(1023 , -1, -1):
            led13.duty(i)
            time.sleep_ms(2)

if __name__=="__main__":
    main()