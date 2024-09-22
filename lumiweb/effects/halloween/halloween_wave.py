import math
import random
import time

from lumiweb.effects.effect import Effect
from lumiweb.effects.halloween import PURPLE, PURPLE_DIM, ORANGE, ORANGE_DIM, GREEN, GREEN_DIM


class HalloweenWave(Effect):

    BRIGHT_COLOR_ROTATION = [PURPLE, ORANGE, GREEN]
    COLOR_ROTATION = [PURPLE_DIM, ORANGE_DIM, GREEN_DIM]

    def run(self):
        indices_to_light = [i for i in range(0, self.strip.num_pixels)]
        for i in indices_to_light:
            self.strip.pixels[i] = PURPLE_DIM
        self.strip.update()

        # Must be even!
        wave_length = 36
        wave_center = 0
        wave_speed = 5

        reverse = False

        previous_color = PURPLE_DIM        
        current_color = ORANGE_DIM
        current_color_bright = ORANGE

        while not self.strip.stop_animation_flag:
            
            wave_start = wave_center - (wave_length / 2)
            if wave_start < 0:
                wave_start = 0
            
            wave_end = wave_center + (wave_length / 2)
            if wave_end > self.strip.num_pixels:
                wave_end = self.strip.num_pixels

            for i in indices_to_light:
                if self.strip.stop_animation_flag:
                    return

                if i < wave_start:
                    self.strip.pixels[i] = previous_color if reverse else current_color
                elif wave_start <= i <= wave_end:
                    self.strip.pixels[i] = current_color_bright
                else:
                    self.strip.pixels[i] = current_color if reverse else previous_color

            self.strip.update()

            if reverse:
                wave_center -= wave_speed
            else:
                wave_center += wave_speed

            prev_reverse = reverse

            # At the end, send back
            if wave_center >= self.strip.num_pixels + wave_length:
                self.strip.pause(3)
                reverse = True

            # Back at the beginning
            if wave_center <= 0 - wave_length:
                self.strip.pause(3)
                reverse = False

            if prev_reverse != reverse:
                # At an endpoint, switch the colors
                curr_color_index = self.__class__.COLOR_ROTATION.index(current_color)
                new_color_index = curr_color_index + 1

                if new_color_index >= len(self.__class__.COLOR_ROTATION):
                    new_color_index = 0
                
                previous_color = current_color
                current_color = self.__class__.COLOR_ROTATION[new_color_index]
                current_color_bright = self.__class__.BRIGHT_COLOR_ROTATION[new_color_index]
