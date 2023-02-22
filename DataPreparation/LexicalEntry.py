
class LexicalEntry:
    def __init__(self, german='', latin='', lexis=0):
        self.german = german
        self.latin = latin
        self.lexis = lexis

    def __str__(self):
        return f"{self.german}: {self.latin} ({self.lexis})"

    def smart_add(self, entry_value):
        if self.german:
            if self.latin:
                self.lexis = entry_value
            else:
                self.latin = entry_value
        else:
            self.german = entry_value

    def as_dic(self):
        d = {"german": self.german, "latin": self.latin, "lexis": self.lexis}
        return d

    def empty(self):
        return not(self.german and self.latin and self.lexis)


if __name__ == "__main__":
    entry = LexicalEntry('Haus', 'domus', 1)
    print(entry)

