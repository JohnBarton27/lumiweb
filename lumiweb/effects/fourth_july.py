import time

from lumiweb.effects.effect import Effect


class FourthJuly(Effect):

    def __init__(self, strip, stripe_width: int = 5):
        super().__init__(strip)
        self.stripe_width = stripe_width

    def set_candy_cane_stripes(self, offset=0):
        for i in range(self.strip.num_pixels):
            if ((i + offset) // self.stripe_width) % 2 == 0:
                color = (255, 0, 0)  # Red
            else:
                color = (128, 128, 128) # White

            self.strip.pixels[i] = color

        self.strip.update()

    def set_flag(self):
        for i in range(0, 70):
            if i % 5 == 0 or (i + 1) % 5 == 0:
                color = (128, 128, 128)
            else:
                color = (0, 0, 255) # Blue
            self.strip.pixels[i] = color
        
        for i in range(70, 90):
            color = (255, 0, 0) # Red
            self.strip.pixels[i] = color

        for i in range(90, 110):
            color = (128, 128, 128) # White
            self.strip.pixels[i] = color

        for i in range(110, 130):
            color = (255, 0, 0) # Red
            self.strip.pixels[i] = color

        for i in range(130, 150):
            color = (128, 128, 128) # White
            self.strip.pixels[i] = color

        for i in range(150, 170):
            color = (255, 0, 0) # Red
            self.strip.pixels[i] = color

        for i in range(170, 190):
            color = (128, 128, 128) # White
            self.strip.pixels[i] = color

        self.strip.update()

    def run(self):
        self.set_flag()
            
