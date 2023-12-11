import math
import random
import time

from lumiweb.effects.effect import Effect


class AmberTwinkle(Effect):

    AMBER = (255, 120, 10)
    AMBER_DIM = (64, 30, 2)

    def run(self):
        indices_to_light = [i for i in range(0, self.strip.num_pixels, 4)]
        for i in indices_to_light:
            self.strip.pixels[i] = self.__class__.AMBER_DIM
        self.strip.update()

        while not self.strip.stop_animation_flag:
            pixels_to_flash = random.sample(indices_to_light, math.floor(self.strip.num_pixels/10))

            self.strip.fade_pixels(pixels_to_flash, 
                                   starting_color=self.__class__.AMBER_DIM, 
                                   target_color=self.__class__.AMBER)

            time.sleep(0.5)
            self.strip.fade_pixels(pixels_to_flash, 
                                   starting_color=self.__class__.AMBER, 
                                   target_color=self.__class__.AMBER_DIM)
            
            time.sleep(3)            
