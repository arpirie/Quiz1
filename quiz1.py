class HiLo():
    def __init__(self, v=1):
        self.v = v

    def guess(self, n):
        if n < self.v:
            return -1
        if n == self.v:
            return 0
        if n > self.v:
            return 1

# the Hangman game


class Hangman():
    def __init__(self, s="testing"):
        self.word = s
        self.turns = 0
        self.current = len(s) * "_"

    def guess(self, letter):
        n = self.word.find(letter)
        self.turns = self.turns + 1
        while n > -1:
            self.current = self.current[0:n] + self.word[n] + self.current[n+1:]
            new_word = self.word[n+1:]
            new_word_n = new_word.find(letter)
            if new_word_n == -1:
                break
            else:
                n = n + 1 + new_word_n
        if self.word == self.current:
            return "Congratulations! You won!"
        return self.current


