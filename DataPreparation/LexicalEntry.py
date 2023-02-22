
class LexicalEntry:
    def __init__(self, german='', latin='', lexis=0):
        self.german = german
        self.latin = latin
        self.lexis = lexis

    def __str__(self):
        return f"{self.german}: {self.latin} ({self.lexis})"


if __name__ == "__main__":
    entry = LexicalEntry('Haus', 'domus', 1)
    print(entry)

