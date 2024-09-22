from fastapi import APIRouter

from lumiweb.effects.generic.chase import Chase
from lumiweb.effects.halloween import PURPLE, ORANGE

from main import STRIP, set_current_pattern

router = APIRouter(
    prefix="/halloween",
    tags=["halloween"],
    responses={404: {"description": "Not found"}},
)


@router.get("/chase")
async def halloween_chase():
    effect = Chase(STRIP, [PURPLE, ORANGE])
    STRIP.set_animation(effect.run)
    set_current_pattern("Halloween Chase")
    return "Running Halloween Chase effect..."
