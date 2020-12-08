"""Word Finder: finds random words from a dictionary."""
from random import choice as random_word


class WordFinder:
    """
    Given file containing words on individual lines, produces the following as needed:
    -random word out of that list

    >>> wf = WordFinder("words.txt")
    3 words read
    """
    def __init__(self, path):
    
        self.path = path
        self.word_list = open(path, 'r').read().splitlines()
    
    def random(self):
        return random_word(self.word_list)

class SpecialWordFinder(WordFinder):
    """
    Subclass of WordFinder
    Given file containing words, removing lines that contain no content and removing lines that contain comments
    Produces the following as needed: 
    -random word out of that list
    """
    def __init__(self, path):
        super().__init__(path)
        self.word_list = [word for word in self.word_list if ("#" not in word) and (word != "")]


