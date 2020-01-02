from parsers import get_bash_anek
import random


def main():
    sources = [get_bash_anek, get_bash_anek]
    text = -1
    while text == -1:
        parser_index = random.randint(0, len(sources))
        parser = sources[parser_index]
        text = parser()
    print(text)


if __name__ == '__main__':
    main()
