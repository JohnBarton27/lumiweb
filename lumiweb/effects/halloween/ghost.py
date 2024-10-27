from datetime import datetime, timedelta
import time

from lumiweb.effects.effect import Effect


class Ghost(Effect):

    def run(self):
        distance_between = 60
        ghost = [
            (10, 10, 10),
            (10, 10, 10),
            (10, 10, 10),
            (50, 50, 50),
            (50, 50, 50),
            (50, 50, 50),
            (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255)]
        num_pixels = len(ghost)

        offset = 0

        while not self.strip.stop_animation_flag:
            for i in range(0, self.strip.num_pixels):
                if i - offset < num_pixels and (i - offset) >= 0:
                    # First Ghost
                    self.strip.pixels[i] = ghost[i - offset]
                elif i - offset + distance_between < num_pixels and (i - offset + distance_between) >= 0:
                    # Second Ghost
                    self.strip.pixels[i] = ghost[i - offset + distance_between]
                elif i - offset + (distance_between * 2) < num_pixels and (i - offset + (distance_between * 2)) >= 0:
                    # Second Ghost
                    self.strip.pixels[i] = ghost[i - offset + (distance_between * 2)]
                else:
                    self.strip.pixels[i] = (0, 0, 0)

            self.strip.update()

            offset += 1

            if offset >= self.strip.num_pixels + (distance_between  * 2) + 1:
                offset = 0
                now = datetime.now()
                end = now + timedelta(seconds=10)
                while datetime.now() < end:
                    if self.strip.stop_animation_flag:
                        return
                    
                    time.sleep(0.01)
