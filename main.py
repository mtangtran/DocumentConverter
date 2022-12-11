from inputConvert import inputConvert
from datetime import date

# initialize the variable.
pdf = inputConvert()

# Set the font
pdf.setFileFont("Arial", 12)

# Add the date
#pdf.addLine(str(date.today()), "C")

try:
    user_choice = int(input("PLease choose 1 for text file or 2 for user input?"))
except FileNotFoundError:

    quit()

user_value = input("Please enter a text file or user input.")

# Add a line into document
#pdf.addLine("Hello World!", "C")
pdf.addTextFile("check.txt")

# create the pdf
pdf.getPDF("hello.pdf")
