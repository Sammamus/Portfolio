import json
from random import randint


class GenPassphrase:

    def __init__(self):
        self.dice_range = (1, 6)
        self.size_to_num_dict = {
            "large": 5,
            "general_short": 4,
            "short": 4
        }
        self.word_dictionary = "word_dictionaries.json"

    def __call__(self, size, word_count):
        self.size = size
        self.word_count = word_count

        print(self._generate_passphrase())

    def _generate_passphrase(self):
        full_password = []

        for word in range(self.word_count):
            full_password.append(self._generate_word())

        full_password = "-".join(full_password)

        return full_password

    def _generate_word(self):
        word_build = []
        output = ""

        for i in range(self.size_to_num_dict[self.size]):
            word_build.append(str(randint(1, 6)))

        word_build = "".join(word_build)

        with open(self.word_dictionary) as f:
            data = json.load(f)

            output = data[self.size][word_build]

        return output


gp = GenPassphrase()
gp("large", 5)
gp("large", 3)
gp("general_short", 6)
gp("general_short", 2)
gp("short", 4)
gp("short", 7)