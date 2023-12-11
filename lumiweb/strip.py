from datetime import datetime, timedelta
import neopixel
import threading
import time


class Strip:

    def __init__(self, gpio_pin, num_pixels, pixel_order):
        self.gpio_pin = gpio_pin
        self.num_pixels = num_pixels
        self.pixel_order = pixel_order
        self.pixels = None
        self.stop_animation_flag = None
        self.thread = None

        self._setup()

    def _setup(self):
        self.pixels = neopixel.NeoPixel(self.gpio_pin, 
                                        self.num_pixels, 
                                        bpp=3, 
                                        auto_write=False, 
                                        brightness=1, 
                                        pixel_order=self.pixel_order)

    def _stop_current_animation(self):
        if self.thread:
            self.stop_animation_flag = True
            self.thread.join()

            self.thread = None
            self.stop_animation_flag = False

        self.pixels.fill((0, 0, 0))
        self.pixels.show()

    def pause(self, seconds: float):
        now = datetime.now()
        target = now + timedelta(seconds=seconds)

        while target < datetime.now() and not self.stop_animation_flag:
            time.sleep(0.05)

    def set_full_color(self, color):
        self._stop_current_animation()
        self.pixels.fill(color)
        self.pixels.show()

    def fade_pixels(self, pixel_indices: list, 
                    starting_color, target_color):
        num_steps = 25

        r_delta_per_step = (target_color[0] - starting_color[0])/num_steps
        g_delta_per_step = (target_color[1] - starting_color[1])/num_steps
        b_delta_per_step = (target_color[2] - starting_color[2])/num_steps

        for i in range(0, num_steps):
            if self.stop_animation_flag:
                break

            for pixel in pixel_indices:
                new_r = starting_color[0] + (r_delta_per_step * i)
                new_g = starting_color[1] + (g_delta_per_step * i)
                new_b = starting_color[2] + (b_delta_per_step * i)
                self.pixels[pixel] = (new_r, new_g, new_b)
            
            self.pixels.show()

    def update(self):
        self.pixels.show()

    def set_animation(self, effect):
        self._stop_current_animation()

        self.thread = threading.Thread(target=effect)
        self.thread.start() 
