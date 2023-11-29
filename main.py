import board
from fastapi import FastAPI
import neopixel

from lumiweb.strip import Strip
from lumiweb.effects.candy_cane import CandyCane
from lumiweb.effects.rgb_twinkle import RgbTwinkle


app = FastAPI()

NUM_PIXELS = 148
GPIO_PIN = board.D12

STRIP = None


def setup():
    global STRIP
    STRIP = Strip(GPIO_PIN, NUM_PIXELS, pixel_order=neopixel.GRB)


@app.get("/color/{color}")
async def set_color(color: str):
    print("SETTING COLOR...")
    if color == "RED":
        STRIP.set_full_color((255, 0, 0))
    elif color == "GREEN":
        STRIP.set_full_color((0, 255, 0))
    elif color == "BLUE":
        STRIP.set_full_color((0, 0, 255))
    elif color == "OFF":
        STRIP.set_full_color((0, 0, 0))

    return f"Setting full strip to {color}..."



# EFFECTS

@app.get("/effect/candycane")
async def candy_cane():
    effect = CandyCane(STRIP, stripe_width=10)
    STRIP.set_animation(effect.run)
    return "Running candy cane effect..."


@app.get("/effect/rgbtwinkle")
async def rgb_twinkle():
    effect = RgbTwinkle(STRIP)
    STRIP.set_animation(effect.run)
    return "Running RGB Twinkle effect..."


if __name__ == "__main__":
    import uvicorn

    setup()

    STRIP.set_full_color((0, 0, 0))

    # Default effect
    # effect = CandyCane(strip, stripe_width=10)
    # effect.run()

    uvicorn.run(app, host="0.0.0.0", port=8000)
