import requests as rq
import html
import re
import random


class Bash():
    def __init__(self):
        pass

    def get_text(self, url):
        res = rq.request('GET', url=url)
        return res, res.text

    def clear_text(self, text):
        start = text.find('#21201e">') + 9
        end = text.find('/div>')
        text = text[start: end] + 'br>'
        text = text.replace("<' + 'br>", '\n')
        text = html.unescape(text)
        return text

    def get_anek(self, url='https://bash.im/forweb/?u'):
        res, raw = self.get_text(url)
        if res.status_code != 200:
            return -1
        text = self.clear_text(raw)
        return text

    def get_name(self):
        return 'Bash.im'


class AnekdotRu():
    def __init__(self):
        self.possible_tags = [
            'apple',
            'telegram',
            'windows',
            'Билл Гейтс',
            'ии',
            'интернет',
            'программист'
        ]

    def get_text(self, url):
        headers = {'user-agent': 'nice try'}
        res = rq.request('GET', url=url, headers=headers)
        return res, res.text

    def clear_anek(self, anek):
        anek = anek[13:-6]
        anek = anek.replace('<br>  ', ' ')
        anek = anek.replace('<br>-', '\n-')
        anek = anek.replace('<br>', ' ')
        anek = html.unescape(anek)
        return anek

    def get_anek(self):
        tag = self.possible_tags[random.randint(0, len(self.possible_tags) - 1)]
        page = random.randint(1, 5)
        url = 'https://pda.anekdot.ru/tags/{}/{}?type=anekdots&sort=sum'.format(tag, page)
        res, raw = self.get_text(url)
        if res.status_code != 200:
            return -1
        alls = re.findall('class="text">.*?</div>', raw)
        alls = [self.clear_anek(anek) for anek in alls]
        anek_number = random.randint(0, len(alls) - 1)
        return alls[anek_number]

    def get_name(self):
        return 'anekdot.ru'


class Nekdo():
    def __init__(self):
        self.possible_tags = [
            'internet',
            'life',
        ]

    def get_text(self, url):
        res = rq.request('GET', url=url)
        return res, res.text

    def clear_anek(self, anek):
        anek = anek[3:-6]
        anek = anek.replace('<br>', '\n')
        anek = html.unescape(anek)
        return anek

    def get_anek(self):
        tag = self.possible_tags[random.randint(0, len(self.possible_tags) - 1)]
        page = random.randint(1, 80)  # 80 - last page for internet
        url = 'https://nekdo.ru/{}/{}'.format(tag, page)
        res, raw = self.get_text(url)
        if res.status_code != 200:
            return -1
        alls = re.findall('[0-9]">.*?</div>', raw)  # anek
        alls = [self.clear_anek(anek) for anek in alls]
        cats = re.findall('<div class="cat">.*?</div>', raw)  # anek's categories
        ban = ['policy' in cat or 'vulgar' in cat or 'religion' in cat or 'national' in cat for cat in cats]
        anek_number = random.randint(0, len(alls) - 1)
        max_tries = 20
        while ((len(alls[anek_number]) < 5 or ban[anek_number] is True) and max_tries > 0):
            anek_number = random.randint(0, len(alls) - 1)
            max_tries -= 1
        return alls[anek_number]

    def get_name(self):
        return 'nekdo.ru'
