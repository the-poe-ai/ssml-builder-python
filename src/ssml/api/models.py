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
    elements: List[ElementIn]

class SsmlResponse(BaseModel):
    ssml: str