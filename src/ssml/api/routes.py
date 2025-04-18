from fastapi import APIRouter
from .models import SsmlRequest, SsmlResponse
from ..core import SsmlBuilder

router = APIRouter()

@router.post("/ssml", response_model=SsmlResponse)
def generate_ssml(req: SsmlRequest):
    b = SsmlBuilder()
    for el in req.elements:
        if el.type == "text" and el.text:
            b.text(el.text)
        elif el.type == "break":
            b.break_time(strength=el.strength or "medium", time=el.time)
        elif el.type == "say_as" and el.text and el.interpret_as:
            b.say_as(el.text, el.interpret_as, el.format)
    return SsmlResponse(ssml=b.build())