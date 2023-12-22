from lumiweb.effects.effect import Effect


class RGBChase(Effect):

    def __init__(self, strip, stripe_width: int = 2):
        super().__init__(strip)
        self.stripe_width = stripe_width

    def set_stripes(self, offset=0):
        for i in reversed(range(self.strip.num_pixels)):
            if ((i - offset) // self.stripe_width) % 6 == 0:
                color = (255, 0, 0)  # Red
            elif ((i - offset) // self.stripe_width) % 6 == 2:
                color = (0, 255, 0)  # Green
            elif ((i - offset) // self.stripe_width) % 6 == 4:
                color = (0, 0, 255)  # Blue
            else:
                color = (0, 0, 0) # OFF

            self.strip.pixels[i] = color

        self.strip.update()


    def run(self):
        offset = 0

        while not self.strip.stop_animation_flag:
            self.set_stripes(offset)
            offset += 1

            self.strip.pause(0.25)
