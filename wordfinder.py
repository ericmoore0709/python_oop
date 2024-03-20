from random import randint


class WordFinder:
    """Word Finder: finds random words from a dictionary.
        >>> wf = WordFinder("words.txt")
        235886 words read.

        >>> len(wf.words) > 1
        True

        >>> len(wf.random()) > 1
        True
    """

    def __init__(self, filename):
        "Initializes word finder with words from given filename."
        self.words = self.__read_words__(filename)
        print(f"{len(self.words)} words read.")
    
    def __read_words__(self, filename) -> list:
        "Parses words from file (given filename) and returns list of words."
        words = []
        file = open(filename)
        for x in file:
            if x.strip():
                words.append(x.strip())
        file.close()
        return words
    
    def random(self):
        "Selects a pseudorandom word from the list of words."
        indx = randint(0, len(self.words) - 1)
        return self.words[indx]