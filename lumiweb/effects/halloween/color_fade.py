import math
import random
import time
from datetime import datetime, timedelta

from lumiweb.effects.effect import Effect
from lumiweb.effects.halloween import RED, PURPLE, ORANGE, GREEN


class HalloweenColorFade(Effect):

    PIXEL_SPACING = 1

    def fade_in(self, pixels, color, num_steps, delay):
        for step in range(0, num_steps):
            for i in pixels:
                fading_color = ((color[0] / num_steps) * step, (color[1] / num_steps) * step, (color[2] / num_steps) * step) 
                self.strip.pixels[i] = fading_color

            self.strip.update()

            if self.strip.stop_animation_flag:
                return

            time.sleep(delay)

    def fade_out(self, pixels, color, num_steps, delay):
        for step in range(0, num_steps):
            for i in pixels:
                color = (0, 0, 0) if step == num_steps - 1 else color
                fading_color = (color[0] - (color[0] / num_steps) * step, color[1] - (color[1] / num_steps) * step, color[2] - (color[2] / num_steps) * step) 
                self.strip.pixels[i] = fading_color

            self.strip.update()

            if self.strip.stop_animation_flag:
                return

            time.sleep(delay)

    def pause(self, duration):
        now = datetime.now()
        end = now + timedelta(milliseconds=duration)
        while datetime.now() < end:
            if self.strip.stop_animation_flag:
                return
            
            time.sleep(0.01)

    def run(self):
        # assign colors
        affected_pixels = []
        for i in range(0, self.strip.num_pixels, HalloweenColorFade.PIXEL_SPACING):
            # Every X pixel
            affected_pixels.append(i)

        color_order = [RED, PURPLE, GREEN]

        while not self.strip.stop_animation_flag:

            for color in color_order:

                self.fade_in(affected_pixels, color, 100, 0.005)
                self.pause(1000)
                self.fade_out(affected_pixels, color, 100, 0.005)                
                self.pause(1000)
