from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """A subclass of the WordFinder which filters out comments from the given textfile.
    
        >>> swf = SpecialWordFinder("special_words.txt")
        6 words read.
        4 words remain after cleaning.

        >>> len(swf.words) > 1
        True

        >>> len(swf.random()) > 1
        True
    
    """

    def __init__(self, filename):
        "Initializes the SpecialWordFinder with words from the given filename (with comments filtered out)."
        super().__init__(filename)
        self.__clean__()
    
    def __clean__(self):
        "Filters out commented lines from self.words"
        new_list = []
        for x in self.words:
            if '# ' not in x:
                new_list.append(x)
        self.words = new_list
        print(f"{len(new_list)} words remain after cleaning.")