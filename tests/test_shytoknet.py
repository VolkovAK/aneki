from aneki import parsers


def test_source():
    source = parsers.ShytokNet()
    res, text = source.get_text(source.get_url())
    assert res == 200
    cleaned = source.clear_anek(text)
    assert text != cleaned
