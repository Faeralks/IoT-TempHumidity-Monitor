import network
import socket
import time
from urllib.parse import urlparse
from secrets import values
import led

def wifi_connect(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    ip = None
    if not wlan.isconnected():
        wlan.active(True)
        wlan.config(pm=0xa11140)
        wlan.connect(ssid, password)
        ip = wlan.ifconfig()[0]
    return ip

def http_get(url):
    url_components = urlparse(url)
    host = url_components.netloc
    path = url_components.path if url_components.path else '/'
    request = f'GET {path} HTTP/1.0\r\nHost: {host}\r\n\r\n'
    addr = socket.getaddrinfo(host, 80)[0][-1]

    with socket.socket() as s:
        s.connect(addr)
        s.send(bytes(request, 'utf8'))
        time.sleep(1)
        while True:
            data = s.recv(1000)
            if data:
                print(str(data, 'utf8'), end='')
            else:
                break

def main():
    led.test_led()
    try:
        wifi_connect(values['ssid'], values['pw'])
    except KeyboardInterrupt:
        print("Keyboard interrupt")
    except Exception as err:
        print(f"Connection exception: {err}")

    try:
        http_get('http://example.com')
    except Exception as err:
        print(f"HTTP request exception: {err}")

main()