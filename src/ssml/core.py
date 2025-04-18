from typing import List
from .elements import SsmlElement

class SsmlBuilder:
    def __init__(self):
        self._elements: List[SsmlElement] = []

    def add(self, element: SsmlElement) -> "SsmlBuilder":
        self._elements.append(element)
        return self

    def text(self, text: str) -> "SsmlBuilder":
        from .elements import PlainText
        return self.add(PlainText(text))

    def break_time(self, strength: str = "medium", time: str = None) -> "SsmlBuilder":
        from .elements import Break
        return self.add(Break(strength=strength, time=time))

    def say_as(self, text: str, interpret_as: str, format: str = None) -> "SsmlBuilder":
        from .elements import SayAs
        return self.add(SayAs(text, interpret_as, format))

    def build(self, pretty: bool = True) -> str:
        parts = [e.render() for e in self._elements]
        inner = "\n".join(parts)
        if pretty:
            inner = "\n".join("  " + line for line in inner.splitlines())
        return f"<speak>\n{inner}\n</speak>"