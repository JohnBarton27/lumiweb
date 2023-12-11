import math
import random
import time

from lumiweb.effects.effect import Effect


class AreaTesting(Effect):

    AMBER = (255, 120, 10)
    AMBER_DIM = (64, 30, 2)

    def run(self):
        driveway = range(0, 200)
        living_room = range(200, 333)
        pitch = range(333, 423)
        office = range(423, 582)

        for i in driveway:
            self.strip.pixels[i] = (255, 0, 0)

        for i in living_room:
            self.strip.pixels[i] = (0, 255, 0)
        
        for i in pitch:
            self.strip.pixels[i] = (0, 0, 255)

        for i in office:
            self.strip.pixels[i] = (0, 128, 128)

        self.strip.update()

        self.strip.pause(3)

        for i in driveway:
            self.strip.pixels[i] = (0, 255, 0)

        for i in living_room:
            self.strip.pixels[i] = (0, 0, 255)
        
        for i in pitch:
            self.strip.pixels[i] = (0, 64, 64)

        for i in office:
            self.strip.pixels[i] = (255, 0, 0)

        self.strip.update()
