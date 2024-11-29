import time
import board
import digitalio
import neopixel
from rainbowio import colorwheel


class LED:
    def __init__(self, brightness=0.5):
        self.num_pixels = 16
        self.pixels = neopixel.NeoPixel(board.GP0, self.num_pixels)
        self.pixels.brightness = brightness
        self.solid = Solid()

    def set_leds(self, rgb):
        self.pixels.fill(rgb)

    def rainbow(self, speed=0):
        for j in range(255):
            for i in range(self.num_pixels):
                pixel_index = (i * 256 // self.num_pixels) + j
                self.pixels[i] = colorwheel(pixel_index & 255)
            self.pixels.show()
            time.sleep(speed)


class Solid:
    def __init__(self):
        rgb = (0, 0, 0)
        
    def set_rgb(self, r, g, b):
        self.rgb = (r, g, b)


led = LED(brightness=0.1)

while True:
    rgb = input('Insert RGB values seperated by commas: ')
    rgb = [int(i) for i in rgb.split(',')]
    led.set_leds(rgb)
