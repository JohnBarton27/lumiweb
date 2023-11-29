import board
from datetime import datetime
from fastapi import FastAPI
import neopixel
import random
import sys
import time

from lumiweb.strip import Strip

app = FastAPI()

NUM_PIXELS = 148
GPIO_PIN = board.D12

strip = None

def setup():
    global strip
    strip = Strip(GPIO_PIN, NUM_PIXELS, pixel_order=neopixel.GRB)


# Define a route to get a list of items
@app.get("/color/{color}")
async def set_color(color: str):
    if color == "RED":
        strip.set_full_color((255, 0, 0))
    elif color == "GREEN":
        strip.set_full_color((0, 255, 0))
    elif color == "BLUE":
        strip.set_full_color((0, 0, 255))
    elif color == "OFF":
        strip.set_full_color((0, 0, 0))

    return f"Setting full strip to {color}..."

if __name__ == "__main__":
    import uvicorn

    setup()

    strip.set_full_color((0, 0, 0))

    # Run the FastAPI application using Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
