from PyPDF2 import PdfReader
import json

from Nezuko.DataPreparation.LexicalEntry import LexicalEntry


class PDFVocReader:
    def __init__(self):
        self.entries = []
        self.current_entry = LexicalEntry()

    def read_pdf(self, filename, page=None):
        self.entries = []
        self.current_entry = LexicalEntry()
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
                if not self.current_entry.empty():
                    self.entries.append(self.current_entry)
                    self.current_entry = LexicalEntry()
            else:
                self.current_entry.smart_add(text.strip())


if __name__ == "__main__":
    wspace = './resources/'
    fname = wspace + 'Campus_C__Wortschatz_I-III.pdf'
    outjson = wspace + 'Campus_C__Wortschatz_I-III.json'
    voc_reader = PDFVocReader()
    dic = voc_reader.read_pdf(fname, page=None)
    result = []
    for e in dic:
        result.append(e.as_dic())
    with open(outjson, 'w') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)
    print('Idle.')

