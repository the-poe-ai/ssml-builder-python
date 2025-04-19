from ssml.elements import PlainText, Break, SayAs


def test_plain_text_escapes():
    e = PlainText("<hello>")
    assert e.render() == "&lt;hello&gt;"


def test_break_defaults():
    b = Break()
    out = b.render()
    assert 'strength="medium"' in out


def test_break_with_time():
    b = Break(time="500ms")
    out = b.render()
    assert 'time="500ms"' in out


def test_say_as_element():
    s = SayAs("2025", interpret_as="digits")
    out = s.render()
    assert '<say-as interpret-as="digits">2025</say-as>' == out
