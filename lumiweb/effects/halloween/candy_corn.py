import time

from lumiweb.effects.effect import Effect
from lumiweb.effects.halloween import ORANGE, WHITE, YELLOW


class CandyCorn(Effect):

    def __init__(self, strip, stripe_width: int = 5):
        super().__init__(strip)
        self.stripe_width = stripe_width

    def set_candy_cane_stripes(self, offset=0):
        for i in range(self.strip.num_pixels):
            if ((i + offset) // self.stripe_width) % 4 == 0:
                color = WHITE
            elif ((i + offset) // self.stripe_width) % 4 == 1:
                color = ORANGE
            elif ((i + offset) // self.stripe_width) % 4 == 2:
                color = YELLOW
            else:
                color = (0, 0, 0)

            self.strip.pixels[i] = color

        self.strip.update()


    def run(self):
        offset = 0

        while not self.strip.stop_animation_flag:
            self.set_candy_cane_stripes(offset)
            offset += 1

            time.sleep(0.05)
            
