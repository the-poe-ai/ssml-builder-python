def indent_text(text: str, level: int = 1, indent_str: str = "  ") -> str:
    return "\n".join(f"{indent_str*level}{line}" for line in text.splitlines())