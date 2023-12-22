from datetime import datetime, timedelta
import time

from lumiweb.effects.effect import Effect


class BlueWhitePattern(Effect):

    def __init__(self, strip, stripe_width: int = 100):
        super().__init__(strip)
        self.stripe_width = stripe_width

    def run(self):
        while not self.strip.stop_animation_flag:
            for i in range(self.strip.num_pixels):
                if i % 8 in [0, 1, 2]:
                    color = (128, 128, 128)  # White
                elif i % 8 in [4, 5, 6]:
                    color = (0, 0, 255)  # Blue
                else:
                    color = (0, 0, 0)  # Off
                
                self.strip.pixels[i] = color

            self.strip.update()

            self.strip.pause(1.5)

            for i in range(self.strip.num_pixels):
                if i % 8 in [0, 1, 2]:
                    color = (0, 0, 255)  # Blue
                elif i % 8 in [4, 5, 6]:
                    color = (128, 128, 128)  # White
                else:
                    color = (0, 0, 0)  # Off
                
                self.strip.pixels[i] = color

            self.strip.update()

            self.strip.pause(1.5)
