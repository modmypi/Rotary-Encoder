from RPi import GPIO
from time import sleep

clk = 17
dt = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
aLastState = GPIO.input(clk)

try:

        while True:
                aState = GPIO.input(clk)
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
