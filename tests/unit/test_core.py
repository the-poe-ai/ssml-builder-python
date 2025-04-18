from ssml.core import SsmlBuilder


def test_builder_renders():
    b = SsmlBuilder().text("Hi").break_time(time="250ms")
    xml = b.build(pretty=False)
    assert xml.startswith("<speak>")
    assert "Hi" in xml
    assert '<break strength="medium" time="250ms"/>' in xml
    assert xml.endswith("</speak>")
