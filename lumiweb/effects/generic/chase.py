from lumiweb.effects.effect import Effect


class Chase(Effect):

    def __init__(self, strip, colors: list, stripe_width: int = 2, pause: float=0.25):
        super().__init__(strip)
        self.colors = colors
        self.stripe_width = stripe_width
        self.pause = pause

    def set_stripes(self, offset=0):
        divisor = len(self.colors) * self.stripe_width

        for i in reversed(range(self.strip.num_pixels)):
            quotient = ((i - offset) // self.stripe_width)
            remainder = quotient % divisor

            if remainder % 2 == 1:
                # This inserts a blank space
                color = (0, 0, 0)
            else:
                color = self.colors[remainder//2]

            self.strip.pixels[i] = color

        self.strip.update()

    def run(self):
        offset = 0

        while not self.strip.stop_animation_flag:
            self.set_stripes(offset)
            offset += 1

            self.strip.pause(self.pause)
