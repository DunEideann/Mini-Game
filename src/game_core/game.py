from utils.game_methods import HangedGameUtils
import random

class GameAPP(object):
    """Class for the game's core features."""
    def __init__(self):
        """Construct for the class GameAPP."""
        self.letters = []
        self.game_status = "running"

    def run_game(self):
        # Leer palabras de archivo y guardar
        words = HangedGameUtils.read_words("utils/words.csv")

        # Elegir una palabra al azar
        word = random.choice(words)

        tries = len(word)+1
        print(f"The word is : {' '+'_ '*len(word)}")

        while self.game_status == "running":
            add_letter = False
            letter = input("Please enter a letter: ")
            add_letter = HangedGameUtils.check_letter(letter, word)
            if add_letter:
                self.letters.append(letter)
            # Mostrar figura y espacios vacios con letras
            first_line, second_line = HangedGameUtils.define_lines(word, self.letters, tries)
            HangedGameUtils.show_output(first_line, second_line)
            if "_" not in second_line:
                self.game_status = "win"
            elif tries <= 0:
                self.game_status = "lose"
            if not add_letter:
                tries -= 1

        if self.game_status == "win":
            print("Felicidades has ganado!")
        elif self.game_status == "lose":
            print("gg wp")