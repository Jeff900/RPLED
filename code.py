import os
import wifi
import socketpool
import time
import board
from adafruit_httpserver import Server, Request, Response
from led import LED


ssid = os.getenv('CIRCUITPY_WIFI_SSID')
password = os.getenv('CIRCUITPY_WIFI_PASSWORD')
print(f"Connecting to {ssid}...")
wifi.radio.connect(ssid, password)
print(f"Connected to {ssid}")
pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, "/static", debug=True)
led = LED()
led.set_leds(led.data['rgb'])


@server.route('/solid')
def solid(request: Request):
    params = dict(request.query_params.items())
    led.set_leds((
        int(params['r']),
        int(params['g']),
        int(params['b'])))
    with open('templates/index.html', 'r') as file:
        html = file.read()
        print(type(html))
    return Response(request, body=html, content_type='text/html')


@server.route('/')
def index(request: Request):
    with open('templates/index.html', 'r') as file:
        html = file.read()
        print(type(html))
    return Response(request, body=html, content_type='text/html')

server.serve_forever(str(wifi.radio.ipv4_address))
