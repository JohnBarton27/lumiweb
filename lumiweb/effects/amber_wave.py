import math
import random
import time

from lumiweb.effects.effect import Effect


class AmberWave(Effect):

    AMBER = (255, 120, 10)
    AMBER_DIM = (64, 30, 2)

    def run(self):
        self.strip.set_full_color((0, 0, 0))
        indices_to_light = [i for i in range(0, self.strip.num_pixels, 4)]
        for i in indices_to_light:
            self.strip.pixels[i] = self.__class__.AMBER_DIM
        self.strip.update()

        # Must be even!
        wave_length = 36
        wave_center = 0
        wave_speed = 5

        reverse = False
        
        while not self.strip.stop_animation_flag:
            
            wave_start = wave_center - (wave_length / 2)
            if wave_start < 0:
                wave_start = 0
            
            wave_end = wave_center + (wave_length / 2)
            if wave_end > self.strip.num_pixels:
                wave_end = self.strip.num_pixels

            for i in indices_to_light:
                if wave_start <= i <= wave_end:
                    self.strip.pixels[i] = self.__class__.AMBER
                else:
                    self.strip.pixels[i] = self.__class__.AMBER_DIM

            self.strip.update()

            if reverse:
                wave_center -= wave_speed
            else:
                wave_center += wave_speed

            if wave_center >= self.strip.num_pixels + wave_length:
                time.sleep(3)
                reverse = True

            if wave_center <= 0 - wave_length:
                time.sleep(3)
                reverse = False

