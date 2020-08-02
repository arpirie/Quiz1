class HiLo():
    def __init__(self, v=1):
        pass

# the Hangman game

class Hangman():
    def __init__(self, s="testing"):
        self.word = s
        self.turns = 0
        self.current = len(s) * "_"

    def guess(self, letter):
        pass  # write the code here to make the tests pass