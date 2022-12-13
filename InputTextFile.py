"""
Convert input to text file
"""

class InputTextFile:

    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, "a")

    def addLine(self, line):
        self.file.write(line)

    def closeFile(self):
        self.file.write("end")
        self.file.close()