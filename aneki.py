from parsers import Bash, AnekdotRu
import random


def main():
    sources = [Bash(), AnekdotRu()]
    text = -1
    while text == -1:
        parser_index = random.randint(0, len(sources) - 1)
        parser = sources[parser_index]
        text = parser.get_anek()
    print(text)


if __name__ == '__main__':
    main()
