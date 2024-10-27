from fastapi import APIRouter

from lumiweb.effects.generic.chase import Chase
from lumiweb.effects.halloween import PURPLE, ORANGE


router = APIRouter(
    prefix="/effect/halloween",
    tags=["halloween"],
    responses={404: {"description": "Not found"}},
)

from lumiweb import globals

@router.get("/chase")
async def halloween_chase():
    from main import set_current_pattern
    effect = Chase(globals.STRIP, [PURPLE, ORANGE])
    globals.STRIP.set_animation(effect.run)
    set_current_pattern("Halloween Chase")
    return "Running Halloween Chase effect..."
