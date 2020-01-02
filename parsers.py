import requests as rq


def get_anek_text(url):
    res = rq.request('GET', url=url)
    return res, res.text


def clear_text(text):
    start = text.find('#21201e">') + 9
    end = text.find('/div>')
    text = text[start: end] + 'br>'
    text = text.replace("<' + 'br>", '\n')
    text = text.replace('&quot;', '"')
    return text


def get_bash_anek(url='https://bash.im/forweb/?u'):
    res, raw = get_anek_text(url)
    if res.status_code != 200:
        return -1
    text = clear_text(raw)
    return text
