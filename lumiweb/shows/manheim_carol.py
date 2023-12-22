import threading

from lumiweb.effects.effect import Effect


class ManheimCarol(Effect):

    # INTRO
    def small_hit(self, pixels, color):
        num_steps = 8

        self.strip.fade_pixels(pixels, (0, 0, 0), color, num_steps)
        self.strip.fade_pixels(pixels, color, (0, 0, 0), num_steps)

    def one_two_three(self, pixels, color):
        num_steps = 4

        self.strip.fade_pixels(pixels, (0, 0, 0), color, num_steps)
        self.strip.fade_pixels(pixels, color, (0, 0, 0), num_steps)

    def four_bells(self, pixels, color):
        num_steps = 2
        self.strip.fade_pixels(pixels, (0, 0, 0), color, num_steps)
        self.strip.fade_pixels(pixels, color, (0, 0, 0), num_steps)

    def fade_in(self):
        pixels = range(0, 200)

        self.strip.fade_pixels(pixels, (0, 0, 0), (128, 128, 128), num_steps=500)

    def run(self):
        OFF = (0, 0, 0)
        PURPLE = (100, 0, 100)

        for _ in range(0, 8):
            self.small_hit(range(377, 379), PURPLE)
        
        for _ in range(0, 4):
            hit1 = list(range(363, 378)) + list(range(378, 393))
            hit2 = list(range(348, 363)) + list(range(393, 408)) 
            hit3 = list(range(334, 348)) + list(range(408, 423)) 

            self.one_two_three(hit1, PURPLE)
            self.one_two_three(hit2, PURPLE)
            self.one_two_three(hit3, PURPLE)

            self.strip.pause(0.05)

        for _ in range(0, 8):
            hit1 = list(range(363, 378)) + list(range(378, 393))
            hit2 = list(range(355, 363)) + list(range(393, 400)) 
            hit3 = list(range(348, 355)) + list(range(400, 408))
            hit4 = list(range(334, 348)) + list(range(408, 423)) 

            self.one_two_three(hit1, PURPLE)
            self.four_bells(hit2, PURPLE)
            self.four_bells(hit3, PURPLE)
            self.one_two_three(hit4, PURPLE)

            self.strip.pause(0.05)

        fade_thread = threading.Thread(target=self.fade_in)
        fade_thread.start()

        for _ in range(0, 8):
            hit1 = list(range(363, 378)) + list(range(378, 393))
            hit2 = list(range(355, 363)) + list(range(393, 400)) 
            hit3 = list(range(348, 355)) + list(range(400, 408))
            hit4 = list(range(334, 348)) + list(range(408, 423)) 

            self.one_two_three(hit1, PURPLE)
            self.four_bells(hit2, PURPLE)
            self.four_bells(hit3, PURPLE)
            self.one_two_three(hit4, PURPLE)

            self.strip.pause(0.05)

