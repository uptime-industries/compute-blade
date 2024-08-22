import time
import board
import busio
from adafruit_emc2101 import EMC2101
import digitalio
import neopixel


g,r,b = 0,0,0
mintemp = 20 # Temperature Boundaries. Closer to this is green. LEDs
maxtemp = 35 # Temperature Boundaries. Closer to this is red. LEDs
LEDbrightness = 0.6 # Yes, you can change the brightness here
baudrate = 115200 # The UART conection speed
timeout = 0 # number of time before timeout

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
pixels = neopixel.NeoPixel(board.GP15, 2, brightness=LEDbrightness, auto_write=False)
pixel_order=neopixel.GRB

button = digitalio.DigitalInOut(board.GP12)

fan_power = digitalio.DigitalInOut(board.GP16) # The fan power control is on GPIO16 you can turn it off/on.
fan_power.direction = digitalio.Direction.OUTPUT
fan_power.value = True

uart = busio.UART(board.GP0, board.GP1, baudrate=baudrate, timeout=timeout)
uart1 = busio.UART(board.GP8, board.GP9, baudrate=baudrate, timeout=timeout)
i2c = busio.I2C(board.GP5, board.GP4) 
emc = EMC2101(i2c)


def show(percent, pixel):
    a = int(round((510 / 100) * percent))
    if a > 255:
        r = 255
        g = 510 - a
    else:
        r = a
        g = 255
    pixels[pixel] = (g, r, b)
    pixels.show()
#    return print('showed', a, 'on', pixel)


while True:
    
    temp = emc.external_temperature        
    if mintemp <= temp <= maxtemp:
        temp = temp - mintemp
        mtemp = maxtemp - mintemp
        c = int(round((temp / mtemp) * 100))
        show(c, 0)
    elif temp < mintemp:
        pixels[0] = (255, 0, 0)
    else:
        pixels[0] = (0, 255, 0)
     
    temp = emc.internal_temperature + 2
    if mintemp <= temp <= maxtemp:
        temp = temp - mintemp
        mtemp = maxtemp - mintemp
        c = int(round((temp / mtemp) * 100))
        show(c, 1)
    elif temp < mintemp:
        pixels[1] = (255, 0, 0)
    else:
        pixels[1] = (0, 255, 0)
    time.sleep(0.1)
    
    dataA = uart.read(8)
    dataB = uart1.read(8)
    #uart.write(bytes(str("Hello Blade A" + "\n"),'UTF-8'))
    #uart1.write(bytes(str("Hello Blade B" + "\n"),'UTF-8'))
    #print (dataA)
    #print (dataB)

    try:
        dataA=int(dataA)
    except:        
        dataA = 'Auto'
    try:
        dataB=int(dataB)
    except:        
        dataB = 'Auto'

#     if dataA is not None:
#         dataA = dataA.decode()
#     if dataB is not None:
#         dataB = dataB.decode()
    if button.value:
        print("Button is not pressed")
    else:
        print("Button pressed")
        
    print("From Blade A", dataA)
    print("From Blade B", dataB)
    
    print("Blade A airflow temperature:", emc.internal_temperature, "C")
    print("Blade B airflow temperature:", emc.external_temperature, "C")
    BladeA_uart_info = bytes(str("Blade A airflow temperature: " + str(emc.internal_temperature) + " C" + "\r\n"),'UTF-8')
    BladeB_uart_info = bytes(str("Blade B airflow temperature: " + str(emc.external_temperature) + " C" + "\r\n"),'UTF-8')
    #BladeA_uart_info = bytes(str(str(emc.external_temperature) + " C" + "\r\n"),"ascii")
    #BladeB_uart_info = bytes(str(str(emc.internal_temperature) + " C" + "\r\n"),"ascii")
    #print(BladeA_uart_info + BladeB_uart_info)
    fan_speed=bytes(str("Fan speed: " + str(emc.fan_speed) + "RPM" + "\r\n" + "\r\n"),'UTF-8')
    blade_request=bytes(str("Blade A: " + str(dataA) + "%" + "| Blade B: " + str(dataB) + "%" + "\r\n"),'UTF-8')
    uart.write(BladeA_uart_info + BladeB_uart_info + blade_request + fan_speed)
    uart1.write(BladeA_uart_info + BladeB_uart_info + blade_request + fan_speed)
    
    if dataA is not 'Auto' and dataB is not 'Auto':
        print("Both blades want to set the temperature")
        print("Blade A asks:", dataA, "%")
        print("Blade B asks:", dataB, "%")
        emc.manual_fan_speed = int(max(dataA, dataB))
        print("Fan speed", emc.fan_speed, "RPM or", int(max(dataA, dataB)), "%")
        time.sleep(2)
        print("")
        continue   
    if (dataA is not 'Auto' and dataB is 'Auto') or (dataA is 'Auto' and dataB is not 'Auto'):  #xor in a hurry
        if dataA is not 'Auto':
            led.value = True
            print("Set the speed as Blade A asks:", dataA, " %")
            emc.manual_fan_speed = int(dataA)
            time.sleep(1)
            print("Fan speed", emc.fan_speed, "RPM")
            time.sleep(1)
        if dataB is not 'Auto':
            led.value = True
            print("Set the speed as Blade B asks:", dataB, " %")
            emc.manual_fan_speed = int(dataB)
            time.sleep(2)
            print("Fan speed", emc.fan_speed, "RPM")
        time.sleep(2)
        print("")
        continue 
        
    else:     
        if 40 <= emc.external_temperature or 40 <= emc.internal_temperature:
            led.value = True
            print("Setting fan speed to 100%")
            emc.manual_fan_speed = 100
            time.sleep(2)
            print("Fan speed", emc.fan_speed, "RPM")
            time.sleep(1)
        elif 35 <= emc.external_temperature < 40 or 35 <= emc.internal_temperature < 40:
            led.value = True
            print("Setting fan speed to 70%")
            emc.manual_fan_speed = 70
            time.sleep(2)
            print("Fan speed", emc.fan_speed, "RPM")
            time.sleep(1)
        elif 33 <= emc.external_temperature < 35 or 33 <= emc.internal_temperature < 35:
            led.value = True
            print("Setting fan speed to 60%")
            emc.manual_fan_speed = 60
            time.sleep(2)
            print("Fan speed", emc.fan_speed, "RPM")
            time.sleep(1)
        elif 31 <= emc.external_temperature < 33 or 31 <= emc.internal_temperature < 33:
            led.value = True
            print("Setting fan speed to 40%")
            emc.manual_fan_speed = 40
            time.sleep(2)
            print("Fan speed", emc.fan_speed, "RPM")
            time.sleep(1)
        elif 29 <= emc.external_temperature < 31 or 29 <= emc.internal_temperature < 31:
           #led.value = True
            print("Setting fan speed to 30%")
            emc.manual_fan_speed = 30
            time.sleep(2)
            print("Fan speed", emc.fan_speed, "RPM")
            time.sleep(1)
        else:
            #led.value = True
            print("Setting fan speed to 10%")
            emc.manual_fan_speed = 10
            time.sleep(2)
            print("Fan speed", emc.fan_speed, "RPM")
            time.sleep(1)
            

    print("")
    time.sleep(1)