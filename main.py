from inputConvert import inputConvert
from datetime import date

# initialize the variable.
pdf = inputConvert()

# Set the font
pdf.setFileFont("Arial", 12)

# Add the date
#pdf.addLine(str(date.today()), "C")

# Add a line into document
#pdf.addLine("Hello World!", "C")
pdf.addTextFile("check.txt")

# create the pdf
pdf.getPDF("hello.pdf")
