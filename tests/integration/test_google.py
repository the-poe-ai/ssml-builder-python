from ssml.providers.google import GoogleSsmlBuilder


def test_google_namespaces():
    b = GoogleSsmlBuilder().text("Test")
    xml = b.build(pretty=False)
    assert 'xmlns="http://www.w3.org/2001/10/synthesis"' in xml
    assert 'xmlns:mstts' in xml
    assert "Test" in xml