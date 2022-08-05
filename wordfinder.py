"""Word Finder: finds random words from a dictionary."""

from math import random


class WordFinder:

    def __init__(self, path):
        data_file = open(path)

        self.words = self.parse(data_file)

        print(f"{len(self.words)} words read")

    
    def parse(self, data_file):
        return [word.strip() for word in data_file]

    def random(self):
        return random.choice(self.words)

class SpecialWordFinder:

    def parse(self, data_file):
        return [word.strip() for word in data_file
                if word.strip() and not word.startswith("#")]
