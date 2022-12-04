from inputConvert import inputConvert

# initialize the variable.
pdf = inputConvert()

# Set the font
pdf.setFileFont("Arial", 12)

# Add a line into document
pdf.addLine("Hello World!", "C")

# create the pdf
pdf.getPDF("hello.pdf")
