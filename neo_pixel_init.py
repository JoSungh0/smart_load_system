import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 8)
pixels.fill((0,0,0))
pixels.show()
