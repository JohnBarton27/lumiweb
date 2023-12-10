import board
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import neopixel

from lumiweb.strip import Strip
from lumiweb.effects.amber_twinkle import AmberTwinkle
from lumiweb.effects.blue_orange import BlueOrange
from lumiweb.effects.candy_cane import CandyCane
from lumiweb.effects.rgb_twinkle import RgbTwinkle


app = FastAPI()

templates = Jinja2Templates(directory="lumiweb/static/templates")
app.mount("/style", StaticFiles(directory="lumiweb/static/style"), name="style")

NUM_PIXELS = 721
GPIO_PIN = board.D18

STRIP = None


def setup():
    global STRIP
    STRIP = Strip(GPIO_PIN, NUM_PIXELS, pixel_order=neopixel.GRB)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # Render the HTML template and pass data to it
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/color/{color}")
async def set_color(color: str, r: int = 0, g: int = 0, b: int = 0):
    print("SETTING COLOR...")
    if color == "RED":
        STRIP.set_full_color((255, 0, 0))
    elif color == "GREEN":
        STRIP.set_full_color((0, 255, 0))
    elif color == "BLUE":
        STRIP.set_full_color((0, 0, 255))
    elif color == "WARMWHITE":
        STRIP.set_full_color((255, 120, 10))
    elif color == "OFF":
        STRIP.set_full_color((0, 0, 0))
    elif color == "CUSTOM":
        STRIP.set_full_color((r, g, b))

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


@app.get("/effect/blueorange")
async def blue_orange():
    effect = BlueOrange(STRIP)
    STRIP.set_animation(effect.run)
    return "Running Blue Orange effect..."


@app.get("/effect/ambertwinkle")
async def amber_twinkle():
    effect = AmberTwinkle(STRIP)
    STRIP.set_animation(effect.run)
    return "Running Amber Twinkle effect..."


if __name__ == "__main__":
    import uvicorn
    import time

    setup()

    STRIP.set_full_color((0, 0, 0))
    time.sleep(1)

    STRIP.set_full_color((255, 120, 10))

    uvicorn.run(app, host="0.0.0.0", port=8000)
