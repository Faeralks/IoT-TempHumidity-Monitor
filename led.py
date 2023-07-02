import machine
import utime

led_red = machine.Pin(15, machine.Pin.OUT)
led_yellow = machine.Pin(14, machine.Pin.OUT)
led_green = machine.Pin(13, machine.Pin.OUT)

def set_led(r, y, g):
    led_red.value(r)
    led_yellow.value(y)
    led_green.value(g)

def test_led():
    led_red.value(0)
    led_yellow.value(0)
    led_green.value(0)
    
    led_red.value(1)
    utime.sleep(0.5)
    led_red.value(0)
    
    led_yellow.value(1)
    utime.sleep(0.5)
    led_yellow.value(0)
    
    led_green.value(1)
    utime.sleep(0.5)
    led_green.value(0)

def get_active_led():
    if led_red.value() == 1:
        return led_red
    elif led_yellow.value() == 1:
        return led_yellow
    elif led_green.value() == 1:
        return led_green
    else:
        return None  # None of the LEDs is on

def set_leds_based_on_temperature_and_humidity(temperature, humidity):
    if temperature > 30 or humidity > 70:
        # High temperature/humidity: turn on red LED, turn off other LEDs
        set_led(1, 0, 0)
    elif temperature < 5 or humidity < 20:
        # Low temperature/humidity: turn on red LED, turn off other LEDs
        set_led(1, 0, 0)
    elif 15 <= temperature <= 25 and 40 <= humidity <= 60:
        # Normal temperature/humidity: turn on green LED, turn off other LEDs
        set_led(0, 0, 1)
    else:
        # Starting to get dangerous: turn on yellow LED, turn off other LEDs
        set_led(0, 1, 0)