import time
import board
import digitalio
import neopixel
from rainbowio import colorwheel
import json


class LED:
    def __init__(self, filename='data.json'):
        self.filename = filename
        self.data = self.get_data()
        self.num_pixels = self.data['num_pixels']
        self.pixels = neopixel.NeoPixel(board.GP0, self.num_pixels)
        self.pixels.brightness = self.data['brightness']
        self.solid = Solid()

    def get_data(self) -> dict:
        """Loads json data from json file and return dict."""
        with open(self.filename, 'r') as file:
            data = json.load(file)
        return data

    def save_data(self):
        """Saves current data to json file."""
        data = {
            'num_pixels': self.num_pixels,
            'brightness': self.pixels.brightness,
            'rgb': self.rgb
        }
        with open(self.filename, 'w') as file:
            json.dump()

    def set_leds(self, rgb):
        self.rgb = rgb
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


def main():
    while True:
        led = LED()
        led.set_leds(led.data['rgb'])
        rgb = input('Insert RGB values seperated by commas: ')
        rgb = [int(i) for i in rgb.split(',')]
        led.set_leds(rgb)
        # led.save_data()

if __name__ == '__main__':
    main()
