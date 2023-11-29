import time

from lumiweb.effects.effect import Effect


class CandyCane(Effect):

    def __init__(self, strip, stripe_width: int = 5):
        super().__init__(strip)
        self.stripe_width = stripe_width

    def set_candy_cane_stripes(self, offset=0):
        for i in range(self.strip.num_pixels):
            if ((i + offset) // self.stripe_width) % 2 == 0:
                color = (255, 0, 0)  # Red
            else:
                color = (255, 255, 255) # White

            self.strip.pixels[i] = color

        self.strip.update()


    def run(self):
        offset = 0

        while not self.strip.stop_animation_flag:
            self.set_candy_cane_stripes(offset)
            offset += 1

            time.sleep(0.5)
            
