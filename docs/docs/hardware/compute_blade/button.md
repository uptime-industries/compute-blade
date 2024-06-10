
# Edge Button
The button is connected to `GPIO20` in the Raspberry PI compute module and can be customized as you like. Can be pressed with a left touch of the Blade latch.

### Example Script
```py
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO20

try:
    while True:
         button_state = GPIO.input(20)
         if button_state == False:
             print('Button Pressed...')
             time.sleep(0.2)
except:
    GPIO.cleanup()
```