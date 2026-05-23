class Reverse:
    def __init__(self, s: str = ""):
        self.s = s

    def get_reversed(self) -> str:
        return self.s[::-1]


user_input = input("Enter a word to reverse: ")
reverser = Reverse(user_input)
reversed_word = reverser.get_reversed()
print(f"Reversed word: {reversed_word}")