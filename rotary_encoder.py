from RPi import GPIO
from time import sleep

a = 17
b = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(a, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(b, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
aLastState = GPIO.input(a)

try:

        while True:
                aState = GPIO.input(a)
                if aState != aLastState:
                        if GPIO.input(b) != aState:
                                counter += 1
                        else:
                                counter -= 1
                        print counter
                aLastState = aState
                sleep(0.01)
finally:
        GPIO.cleanup()
