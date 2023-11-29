from datetime import datetime, timedelta
import time

from lumiweb.effects.effect import Effect


class RgbTwinkle(Effect):

    def run(self):
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

        num_steps = 128
        delay = 0.005

        # assign colors
        affected_pixels = []
        for i in range(0, self.strip.num_pixels, 3):
            # Every third pixel
            affected_pixels.append(i)

        color_index = 0

        # Color assignments
        color_assignments = {}
        for i in affected_pixels:
            color_assignments[i] = colors[color_index]

            color_index += 1
            if color_index >= len(colors):
                color_index = 0

        while not self.strip.stop_animation_flag:

            # Fade in
            for step in range(0, num_steps):
                for i in affected_pixels:
                    color = color_assignments[i]
                    fading_color = ((color[0] / num_steps) * step, (color[1] / num_steps) * step, (color[2] / num_steps) * step) 
                    self.strip.pixels[i] = fading_color

                self.strip.update()

                if self.strip.stop_animation_flag:
                    return

                time.sleep(delay)

            # Wait 0.5 seconds on full brightness
            now = datetime.now()
            end = now + timedelta(milliseconds=500)
            while datetime.now() < end:
                if self.strip.stop_animation_flag:
                    return

                time.sleep(delay)

            # Fade out
            for step in range(0, num_steps):
                for i in affected_pixels:
                    color = (0, 0, 0) if step == num_steps - 1 else color_assignments[i]
                    fading_color = (color[0] - (color[0] / num_steps) * step, color[1] - (color[1] / num_steps) * step, color[2] - (color[2] / num_steps) * step) 
                    self.strip.pixels[i] = fading_color

                self.strip.update()

                if self.strip.stop_animation_flag:
                    return

                time.sleep(delay)
                
            # Wait 0.5 seconds on full darkness
            now = datetime.now()
            end = now + timedelta(seconds=2)
            while datetime.now() < end:
                if self.strip.stop_animation_flag:
                    return

                time.sleep(delay)

