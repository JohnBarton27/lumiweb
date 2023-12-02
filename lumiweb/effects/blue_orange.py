import math
import time

from lumiweb.effects.effect import Effect


class BlueOrange(Effect):

    BLUE = (0, 0, 117)
    ORANGE = (255, 8, 0)

    def __init__(self, strip):
        super().__init__(strip)
    
    def set_blue_orange_waves(self, color):
        middle_index = math.ceil(self.strip.num_pixels / 2)
        offset = 1
        for i in range(middle_index, self.strip.num_pixels):
            self.strip.pixels[i] = color
            self.strip.pixels[middle_index - offset] = color
            self.strip.update()

            time.sleep(0.02)

            if self.strip.stop_animation_flag:
                return
            
            offset += 1

    def run(self):
        while not self.strip.stop_animation_flag:
            self.set_blue_orange_waves(color=self.__class__.BLUE)
            time.sleep(0.2)
            self.set_blue_orange_waves(color=self.__class__.ORANGE)
            time.sleep(0.2)
