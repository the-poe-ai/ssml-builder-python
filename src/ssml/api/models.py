from pydantic import BaseModel
from typing import List, Optional


class ElementIn(BaseModel):
    type: str
    text: Optional[str]
    strength: Optional[str]
    time: Optional[str]
    interpret_as: Optional[str]
    format: Optional[str]


class SsmlRequest(BaseModel):
    # Either the user passes `elements`, or a single `text_block`
    elements: Optional[List[ElementIn]] = None
    text_block: Optional[str] = None
    pause_ms: Optional[str] = "500ms"


class SsmlResponse(BaseModel):
    ssml: str
