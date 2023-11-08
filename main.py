class Book:
    def __init__(self, dir):
        self.__dir = dir
        self.text = self.get_text()

    def get_text(self):
        text = ""

        with open(self.__dir) as f:
            text = f.read()
            f.close()

        return text

    def char_count(self):
        char_counter = {}

        for c in self.text.lower():
            if c in char_counter:
                char_counter[c] += 1
            else:
                char_counter[c] = 1

        return char_counter

    def word_count(self):
        return len(self.text.split())

    def __str__(self):
        report = f"--- Begin report of {self.__dir} ---\n"
        report += f"{self.word_count()} words found in the document\n\n"

        char_counter = self.char_count()
        char_counter_keys = list(char_counter.keys())
        char_counter_keys.sort()

        for k in char_counter_keys:
            if not k.isalpha():
                continue
            report += f"The '{k}' character was found {char_counter[k]} times\n"

        report += "--- End report ---"
        return report

if __name__ == "__main__":
    b = Book("books/frankenstein.txt")
    print(b)

