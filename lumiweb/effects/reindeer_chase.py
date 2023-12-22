from datetime import datetime, timedelta
import time

from lumiweb.effects.effect import Effect


class ReindeerChase(Effect):

    def run(self):
        reindeer = [(255, 0, 0), (128, 128, 128), (255, 0, 0),
                    (0, 0, 0), (0, 0, 0),
                    (255, 120, 10), (255, 120, 10),
                    (0, 0, 0), (0, 0, 0),
                    (255, 120, 10), (255, 120, 10),
                    (0, 0, 0), (0, 0, 0),
                    (255, 120, 10), (255, 120, 10),
                    (0, 0, 0), (0, 0, 0),
                    (255, 0, 0)]
        num_pixels = len(reindeer)

        offset = 0

        while not self.strip.stop_animation_flag:
            for i in range(0, self.strip.num_pixels):
                if i - offset < num_pixels and (i - offset) >= 0:
                    self.strip.pixels[i] = reindeer[i - offset]
                else:
                    self.strip.pixels[i] = (0, 0, 0)

            offset += 1

            if offset >= self.strip.num_pixels:
                offset = 0

        
            self.strip.update()

