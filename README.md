# LumiWeb
LumiWeb is a Python web application for controlling RGB LED strips on a Raspberry Pi. The web application is built to be run directly on the Raspberry Pi & controlled remotely.

## Supported Endpoints/Animations
These endpoints can be triggered via an `HTTP GET` to the given address.

### Colors
Several full colors can be shown on the RGB strip - this will set all pixels on the RGB strip to this color.

Endpoint           | Description
------------------ | ---
`/color/RED`       | Sets all LEDs to RED (255, 0, 0)
`/color/GREEN`     | Sets all LEDs to GREEN (0, 255, 0)
`/color/BLUE`      | Sets all LEDs to BLUE (0, 0, 255)
`/color/WARMWHITE` | Sets all LEDs to a warm white (255, 120, 10)
`/color/OFF`       | Turns all LEDs off (0, 0, 0)
`/color/CUSTOM`    | Sets a custom color using `r`, `g`, and `b` query parameters


### Animations/Effects
Several long-running animations are supported as well:

Endpoint             | Description
-------------------- | ---
`/effect/candycane`  | Creates a moving "candy-cane" pattern (alternating blocks of red & white LEDs)
`/effect/rgbtwinkle` | Turns every 3rd LED either red, green, or blue (in order) and has them all slowly fade on/off on repeat.
`/effect/blueorange` | Creates orange and blue "waves" starting from the center of the LED strip