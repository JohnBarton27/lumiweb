import requests
import board
import neopixel
import time
import random 

NUM_PIXELS = 20

GPIO_PIN = 12


pixels = neopixel.NeoPixel(board.D12, NUM_PIXELS, bpp=3, auto_write=False, brightness=1, pixel_order=neopixel.GRB)

pixels.fill((0,0,0))
pixels.show()

