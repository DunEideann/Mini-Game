import pandas
import subprocess
import os

class HangedGameUtils(object):
    """Class with methods for Hanged Game."""

    def __init__(self, last_name):
        self.last_name = last_name
        self.name = "Samuel"
        self.stuff = "Queso"

    @classmethod
    def read_words(cls, csv_name: str):
        """Read and store words from a file into a list."""
        words = pandas.read_csv(csv_name)
        words_list = []
        for word in words["Word"]:
            words_list.append(word)
        
        return words_list


    @classmethod
    def show_output(cls, first_line, second_line):
        """Print messages in two lines constantly."""
        os.system("clear")
        print(first_line)
        print(second_line)

    @classmethod
    def check_letter(cls, letter: str, word: str):
        """Check if a given letter is in the word."""
        return True if letter in word else False

    @classmethod
    def define_lines(cls, word, letters, tries):
        """Create lines to print based on the word to discover and the current letters."""
        first_line = f"Tries left: {tries}"
        cross_word = []
        for pos, letter in enumerate(word):
            if letter in letters:
                cross_word.append(letter)
            else:
                cross_word.append("_")
        second_line = " ".join(x for x in cross_word)
        print(cross_word)
        return first_line, second_line
