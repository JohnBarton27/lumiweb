import board
from datetime import datetime
from fastapi import FastAPI
import neopixel
import random
import sys
import time

from lumiweb.strip import Strip
from lumiweb.effects.candy_cane import CandyCane

app = FastAPI()

NUM_PIXELS = 148
GPIO_PIN = board.D12

strip = None

def setup():
    global strip
    strip = Strip(GPIO_PIN, NUM_PIXELS, pixel_order=neopixel.GRB)


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

@app.get("/effect/candycane")
async def candy_cane():
    effect = CandyCane(strip, stripe_width=10)
    effect.run()
    return "Running candy cane effect..."


if __name__ == "__main__":
    import uvicorn

    setup()

    strip.set_full_color((0, 0, 0))

    # Default effect
    effect = CandyCane(strip, stripe_width=10)
    effect.run()

    # Run the FastAPI application using Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
