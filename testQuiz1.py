import unittest
from quiz1 import HiLo
from quiz1 import Hangman


# HiLo is the high-low game where repeated guesses
# get responses of 'too low', 'too high', or 'correct'
# For this class called HiLo() 'too low' is -1, 'too high' is 1, and 'correct' is 0
# When you create an instance of this class, you give it the number to guess.
# Each call to the guess method, returns -1, 0, or 1.
# When you create an instance of HiLo, you give it the number to guess.
# This assumes the player is not the one who creates the instance.
# We ignore the problem with realism.
# Since the instance is created with the value 1, the tests check for
# guesses of 0, 1, and 2 making sure we get -1, 0, and 1 respectively.
# uncomment each of the tests below and when they fail, add the code to make
# them pass.  The code should be added in quiz1.py
class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.game = HiLo(1)
    # def test_game(self):
    #     self.assertTrue(self.game.guess(0) == -1)
    #     self.assertTrue(self.game.guess(1) == 0)
    #     self.assertTrue(self.game.guess(2) == 1)


# The Hangman class is a game of hangman where you create an instance by
# giving it the word to guess.  i.e. self.game = Hangman("Apple")
# Then to make a guess you call the guess method
# r = self.game.guess("A")
# guess returns a string like "A____" in this case
# if the first guess was "B", then r would be "_____"
# if the first guess was "e", then r would be "____e"
# making a guess adds to the number of turns.
# you can get the number of turns by looking at self.game.turns
# Hints: You will need two variables inside the class; call them 'current' and 'word'
#        current is the current state (like "A____" or "____e") and word is the word
#        to guess.  ("Apple")  As correct guesses are made, these need to change as
#        follows:  The correct letter is put into current at the correct place and
#        the correct letter is removed from the word.  So if the first guess was "A",
#        then 'word' would become "_pple" and 'current' would be "A____"
#        You can't change strings but you can make new ones from the old.
#        To make "Apple" become "A_ple", if word = "Apple" and current = "_____",
#        then word[0:1] + "_" + word[2:] will create "A_ple"
#        and  current[0:1] + "p" + current[2:] will create "_p___"
#        Knowing this, you can take a guess of a letter and change these variables
#        then return the current one as a result.

class HangmanTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Hangman("Apple")

    # def test_guess(self):
        # s = self.game.guess("A")
        # self.assertTrue(s == "A____", f"{s}")
        # self.assertTrue(self.game.turns == 1,f"{self.game.turns}")
        # self.assertTrue(self.game.guess("B") == "A____")
        # self.assertTrue(self.game.turns == 2)
        # self.assertTrue(self.game.guess("p") == "App__")
        # self.assertTrue(self.game.turns == 3)
        # self.assertTrue(self.game.guess("e") == "App_e")


if __name__ == '__main__':
    unittest.main()
