import time

from lumiweb.effects.effect import Effect


class RedGreenPattern(Effect):

    def __init__(self, strip, stripe_width: int = 100):
        super().__init__(strip)
        self.stripe_width = stripe_width


    def set_stripes(self, offset=0):
        for i in reversed(range(self.strip.num_pixels)):
            if ((i - offset) // self.stripe_width) % 2 == 0:
                color = (255, 0, 0)  # Red
            else:
                color = (0, 255, 0) # Green

            self.strip.pixels[i] = color

        self.strip.update()


    def run(self):
        offset = 0

        while not self.strip.stop_animation_flag:
            self.set_stripes(offset)
            offset += 1

            time.sleep(0.05)
