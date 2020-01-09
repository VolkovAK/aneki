from aneki import parsers


def test_bash():
    bash = parsers.Bash()
    for _ in range(10):
        res, text = source.get_text(source.get_url())
        if res == 200:
            break
    assert res == 200
    cleaned = bash.clear_anek(text)
    assert text != cleaned
