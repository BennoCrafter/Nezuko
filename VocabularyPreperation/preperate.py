from PyPDF2 import PdfReader


class PDFVocReader:
    def __init__(self):
        self.entries = []
        self.current_entry = []

    def read_pdf(self, filename, page=None):
        self.entries = []
        self.current_entry = []
        reader = PdfReader(filename)
        if isinstance(page, int):
            page = reader.pages[int(page)]
            page.extract_text(visitor_text=self.visitor_body)
        else:
            for page in reader.pages:
                page.extract_text(visitor_text=self.visitor_body)
        return self.entries

    def visitor_body(self, text, cm, tm, fontDict, fontSize):
        y = tm[5]
        if 50 < y < 780:
            if text == '\n':
                if len(self.current_entry) > 2:
                    self.entries.append(self.current_entry)
                    self.current_entry = []
            else:
                self.current_entry.append(text.strip())


if __name__ == "__main__":
    fname = 'Campus_C__Wortschatz_I-III.pdf'
    voc_reader = PDFVocReader()
    dic = voc_reader.read_pdf(fname, page=0)
    print(dic)