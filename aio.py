import ubinascii
import machine
from mqtt import MQTTClient
from secrets import values

AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USERNAME = values['AIO_username']
AIO_KEY = values['AIO_key']
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id())

mqtt_client = None

def connect_to_ada():
    global mqtt_client
    if mqtt_client is None:
        try:
            mqtt_client = MQTTClient(AIO_CLIENT_ID, AIO_SERVER, AIO_PORT, AIO_USERNAME, AIO_KEY, keepalive=60)
            mqtt_client.connect()
        except Exception as e:
            print("Failed to connect to Adafruit IO:", e)

def send_data(feed_key, value):
    global mqtt_client
    try:
        if mqtt_client is None:
            connect_to_ada()
        mqtt_client.publish(feed_key, str(value))
    except Exception as e:
        print("Failed to send data to Adafruit IO:", e)
        mqtt_client = None
        connect_to_ada()  
        try:
            mqtt_client.publish(feed_key, str(value))
        except Exception as e:
            print("Failed to send data to Adafruit IO after reconnect:", e)
            mqtt_client = None  