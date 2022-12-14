from fpdf import FPDF

"""
This class allows for the creation of a pdf. 

References:
1. https://www.geeksforgeeks.org/convert-text-and-text-file-to-pdf-using-python/
"""


class inputConvert:

    def __init__(self):
        """
        Constructor initializes the object and starts the first page.
        :return:
        """
        self.pdf = FPDF()
        self.pdf.add_page()
        self.line_counter = 0

    def setFileFont(self, fontType, fontSize):
        """
        Set the font.
        :param fontType: String
        :param fontSize: integer
        :return:
        """
        self.pdf.set_font(fontType, size=fontSize)

    def addLine(self, text, alignment):
        """
        Add another line to the document.
        :param text:
        :param alignment:
        :return:
        """
        self.pdf.cell(200, 100, txt=text, ln=self.line_counter, align=alignment)
        self.line_counter = self.line_counter + 1

    def addTextFile(self, txtfile):
        """
        Inputs a txt file and adds it into the document.
        :param txtfile: txtfilename.
        :return:
        """
        self.pdf.cell(200, 10, txt=txtfile, ln=1, align="C")
        tfile = open(txtfile)
        number = 0
        for x in tfile:
            number = number + 1
            changed_str = str(number) + ". " + x
            self.pdf.cell(200, 10, txt=changed_str, ln=1, align="L")

    def getPDF(self, filename):
        """
        Inputs a string filename
        :param filename: filename
        :return: a pdf with that filename
        """
        return self.pdf.output(filename)
