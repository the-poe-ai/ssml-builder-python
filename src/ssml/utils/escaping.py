import xml.sax.saxutils as saxutils

def escape_text(text: str) -> str:
    return saxutils.escape(text)