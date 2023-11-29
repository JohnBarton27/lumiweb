from datetime import datetime
import requests
import board
import neopixel
import random
import threading
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

CLOCK_PIXELS = 24
EMPTY_PIXELS = 3
PENDULUM_PIXELS = 27
NUM_PIXELS = 148

GPIO_PIN = 12


pixels = neopixel.NeoPixel(board.D12, NUM_PIXELS, bpp=3, auto_write=False, brightness=1, pixel_order=neopixel.GRB)

def translate_rgb(rgb_tuple: tuple):
    red = rgb_tuple[0]
    blue = rgb_tuple[1]
    green = rgb_tuple[2]
    return (green, blue, red)
 

def set_full_color(color):
    pixels.fill(color)
    pixels.show()


def set_color_fade(pixels, color, duration):
    fade_in(pixels, color, duration=duration/2)
    fade_out(pixels, color, duration=duration/2)


def fade_in(pixels, color, duration):    
    fade_steps = int(duration // 0.01)
    step_size_r = color[0] / fade_steps
    step_size_g = color[1] / fade_steps
    step_size_b = color[2] / fade_steps
    current_color = (0, 0, 0)

    for i in range(fade_steps):
        start = datetime.now()
        set_pixels_to_color(pixels, current_color)
        current_color = (current_color[0] + step_size_r,
                         current_color[1] + step_size_g,
                         current_color[2] + step_size_b)
        end = datetime.now()
        time.sleep(0.01 - (end - start).seconds)


def fade_out(pixels, color, duration):    
    fade_steps = int(duration // 0.01)
    step_size_r = color[0] / fade_steps
    step_size_g = color[1] / fade_steps
    step_size_b = color[2] / fade_steps

    for i in range(fade_steps):
        start = datetime.now()
        set_pixels_to_color(pixels, color)
        color = (color[0] - step_size_r,
                color[1] - step_size_g,
                color[2] - step_size_b)
        end = datetime.now()
        time.sleep(0.01 - (end - start).seconds)



def set_pixels_to_color(indexes: list, color, sleep=0):
    for index in indexes:
        pixels[index] = color
    
    pixels.show()
    time.sleep(sleep)


def set_pixel(pixel_index, color):
    # color = translate_rgb(color)
    pixels[pixel_index] = color

def set_candy_cane_stripes(width, offset=0):
    for i in range(NUM_PIXELS):
        if ((i + offset) // width) % 2 == 0:
            color = (255, 0, 0)  # Red
        else:
            color = (255, 255, 255)  # White
        pixels[i] = color
    pixels.show()

def candy_cane(width, delay=0.5):
    offset = 0
    while True:
        set_candy_cane_stripes(width, offset)
        offset += 1
        time.sleep(delay)


def twinkle():
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    delay = 0.05

    for i in range(0, 256, step):
        for i in range(0, NUM_PIXELS, 3):
            color = random.choice(color)
            pixel_color = (int(i * r / 255), int(i * g / 255), int(i * b / 255))
            pixels[i] = random.choice(colors)

        for j in range(0, num_pixels, 3):
            pixels[j] = pixel_color
        pixels.show()
        time.sleep(delay)

    
    pixels.show()




FILE_PATH = "light_command.txt"
stop_flag = False

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self):
        self.current_threads = []

    def process(self, event):
        global stop_flag
        if event.src_path == FILE_PATH:
            for thread in self.current_threads:
                if thread and thread.is_alive():
                    # Terminate the previous thread
                    thread.kill()

            # Read the new contents of the file
            with open(FILE_PATH, 'r') as file:
                content = file.read().strip()

            if content == "off":
                self.current_threads = [TracedThread(target=set_full_color, args=((0,0,0),))]
            else:
                print(f"Unknown command: {content}")
                return
            
            for thread in self.current_threads:
                thread.start()

    def on_modified(self, event):
        self.process(event)


class TracedThread(threading.Thread):
  def __init__(self, *args, **keywords):
    threading.Thread.__init__(self, *args, **keywords)
    self.killed = False
 
  def start(self):
    self.__run_backup = self.run
    self.run = self.__run      
    threading.Thread.start(self)
 
  def __run(self):
    sys.settrace(self.globaltrace)
    self.__run_backup()
    self.run = self.__run_backup
 
  def globaltrace(self, frame, event, arg):
    if event == 'call':
      return self.localtrace
    else:
      return None
 
  def localtrace(self, frame, event, arg):
    if self.killed:
      if event == 'line':
        raise SystemExit()
    return self.localtrace
 
  def kill(self):
    self.killed = True

if __name__ == "__main__":

    set_full_color((0,0,0))

    # candy_cane(10)
    # time.sleep(3)

    twinkle()
    time.sleep(1)
    # event_handler = FileChangeHandler()
    # observer = Observer()
    # observer.schedule(event_handler, path=FILE_PATH, recursive=False)
    # observer.start()

    # try:
    #     while True:
    #         time.sleep(1)
    # except KeyboardInterrupt:
    #     observer.stop()

    # observer.join()
