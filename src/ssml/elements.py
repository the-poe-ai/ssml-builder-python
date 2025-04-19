from abc import ABC, abstractmethod
import xml.sax.saxutils as saxutils
from typing import Optional


class SsmlElement(ABC):
    @abstractmethod
    def render(self) -> str:
        ...


class PlainText(SsmlElement):
    def __init__(self, text: str):
        self.text = saxutils.escape(text)

    def render(self) -> str:
        return self.text


class Break(SsmlElement):
    def __init__(self, strength: str = "medium", time: Optional[str] = None):
        self.strength = strength
        self.time = time

    def render(self) -> str:
        attrs = []
        if self.strength:
            attrs.append(f'strength="{self.strength}"')
        if self.time:
            attrs.append(f'time="{self.time}"')
        return f"<break {' '.join(attrs)}/>"


class SayAs(SsmlElement):
    def __init__(self, text: str, interpret_as: str, format: Optional[str] = None):
        self.text = saxutils.escape(text)
        self.interpret_as = interpret_as
        self.format = format

    def render(self) -> str:
        fmt = f' format="{self.format}"' if self.format else ""
        return f'<say-as interpret-as="{self.interpret_as}"{fmt}>{self.text}</say-as>'
