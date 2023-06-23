"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, path):
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read.")


    def parse(self, dict_file):
        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith('#')]


    def random(self):
        return random.choice(self.words)


wf = WordFinder(r"//wsl.localhost/Ubuntu-22.04/home/izzy_online/pythonprojects/bc_oop_python/python-oo-practice/bootcamp-excercises-22.4/words.txt")
print(f"Random word: {wf.random()}")