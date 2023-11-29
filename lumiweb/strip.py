import neopixel
import threading


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


    def set_full_color(self, color):
        self._stop_current_animation()
        self.pixels.fill(color)
        self.pixels.show()

    def update(self):
        self.pixels.show()

    def set_animation(self, effect):
        self._stop_current_animation()

        self.thread = threading.Thread(target=effect)
        self.thread.start() 