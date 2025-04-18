from ..core import SsmlBuilder


class GoogleSsmlBuilder(SsmlBuilder):
    def build(self, pretty: bool = True) -> str:
        ssml = super().build(pretty=False)
        ns = (
            '<speak xmlns="http://www.w3.org/2001/10/synthesis" '
            'xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">'
        )
        ssml = ssml.replace("<speak>", ns)
        if pretty:
            lines = ssml.splitlines()
            return "\n".join("  " + l for l in lines)
        return ssml
