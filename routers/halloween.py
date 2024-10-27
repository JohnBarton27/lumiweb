from fastapi import APIRouter

from lumiweb import globals
from lumiweb.effects.generic.chase import Chase
from lumiweb.effects.halloween import PURPLE, ORANGE
from lumiweb.effects.halloween.halloween_wave import HalloweenWave
from lumiweb.effects.halloween.candy_corn import CandyCorn
from lumiweb.effects.halloween.color_fade import HalloweenColorFade
from lumiweb.effects.halloween.block_areas import HalloweenBlockAreas
from lumiweb.effects.halloween.ghost import Ghost


router = APIRouter(
    prefix="/effect/halloween",
    tags=["halloween"],
    responses={404: {"description": "Not found"}},
)


from main import set_current_pattern


@router.get("/chase")
async def halloween_chase():
    effect = Chase(globals.STRIP, [PURPLE, ORANGE])
    globals.STRIP.set_animation(effect.run)
    set_current_pattern("Halloween Chase")
    return "Running Halloween Chase effect..."


@router.get("/wave")
async def halloween_wave():
    effect = HalloweenWave(globals.STRIP)
    globals.STRIP.set_animation(effect.run)
    set_current_pattern("Halloween Wave")
    return "Running Halloween Wave effect..."


@router.get("/candycorn")
async def candy_corn():
    effect = CandyCorn(globals.STRIP, stripe_width=10)
    globals.STRIP.set_animation(effect.run)
    set_current_pattern("Candy Corn")
    return "Running candy corn effect..."


@router.get("/colorfade")
async def color_fade():
    effect = HalloweenColorFade(globals.STRIP)
    globals.STRIP.set_animation(effect.run)
    set_current_pattern("Halloween Color Fade")
    return "Running Halloween Color Fade effect..."


@router.get("/blockareas")
async def block_areas():
    effect = HalloweenBlockAreas(globals.STRIP)
    globals.STRIP.set_animation(effect.run)
    set_current_pattern("Halloween Block Areas")
    return "Running Halloween Block Areas effect..."

@router.get("/ghost")
async def ghost():
    effect = Ghost(globals.STRIP)
    globals.STRIP.set_animation(effect.run)
    set_current_pattern("Halloween Ghost")
    return "Running Halloween Ghost effect..."
