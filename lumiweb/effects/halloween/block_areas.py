import time
from datetime import datetime, timedelta
import random

from lumiweb.effects.effect import Effect
from lumiweb.effects.halloween import RED, PURPLE, ORANGE, GREEN, YELLOW
from lumiweb import globals


class HalloweenBlockAreas(Effect):

    PIXEL_SPACING = 1

    def run(self):
        # assign colors

        colors = [ORANGE, PURPLE, GREEN, RED, YELLOW]
        while not self.strip.stop_animation_flag:
            for i in range(globals.GARAGE_START, globals.GARAGE_END + 1):
                self.strip.pixels[i] = colors[0]

            for i in range(globals.LIVING_ROOM_START, globals.LIVING_ROOM_END + 1):
                self.strip.pixels[i] = colors[1]

            for i in range(globals.PITCH_START, globals.PITCH_END + 1):
                self.strip.pixels[i] = colors[2]

            self.strip.update()

            now = datetime.now()
            end = now + timedelta(seconds=5)
            while datetime.now() < end:
                if self.strip.stop_animation_flag:
                    return
                
                time.sleep(0.01)

            # colors.append(colors.pop(0))
            random.shuffle(colors)

