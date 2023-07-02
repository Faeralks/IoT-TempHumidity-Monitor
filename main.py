import machine
import dht
import utime
import aio
import led
from secrets import values

# Initialize DHT11 sensor
dh = dht.DHT11(machine.Pin(27, machine.Pin.OUT))

temperature_feed_key = values['temp_feed_key']
humidity_feed_key = values['humd_feed_key']

# Fetch the interval from credentials or default to 15 seconds
transmission_interval = 15 
last_transmission = 0

def reset():
    utime.sleep(5)
    machine.reset()

def toggle_led(led, delay=0.5):
    if led is not None:
        led.value(not led.value())
        utime.sleep(delay)

def main():
    global last_transmission
    while True:
        current_time = utime.time()
        if (current_time - last_transmission) >= transmission_interval:
            dh.measure()
            temperature = dh.temperature()
            humidity = dh.humidity()

            # Update LED status based on temperature and humidity
            led.set_leds_based_on_temperature_and_humidity(temperature, humidity)

            # Get the currently active LED
            active_led = led.get_active_led()

            # Indicate publishing by toggling the active LED
            toggle_led(active_led)

            # Send data to Adafruit IO
            aio.send_data(temperature_feed_key, temperature)
            aio.send_data(humidity_feed_key, humidity)

            # Toggle the active LED back
            toggle_led(active_led)

            last_transmission = current_time

        utime.sleep(1)  # sleep for 1 second before checking again
    
# Main program
# Connect to Adafruit IO before entering the loop
aio.connect_AIO()
while True:
    try:
        main()
    except Exception as e:
        print('Encountered error:', e)
        reset()