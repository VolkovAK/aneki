from aneki import parsers


def test_bash():
    bash = parsers.Bash()
    res, text = bash.get_text(bash.get_url())
    assert res == 200
    cleaned = bash.clear_text(text)
    assert text != cleaned
