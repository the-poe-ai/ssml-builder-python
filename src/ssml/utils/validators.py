import re

SSML_TIME_PATTERN = re.compile(r"^\d+(ms|s)$")
STRENGTHS = {"none","x-weak","weak","medium","strong","x-strong"}

def validate_break(strength: str = None, time: str = None):
    if strength and strength not in STRENGTHS:
        raise ValueError(f"Invalid SSML strength: {strength}")
    if time and not SSML_TIME_PATTERN.match(time):
        raise ValueError(f"Invalid SSML time format: {time}")