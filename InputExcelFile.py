"""
This class intends to be a resource for adding user input into the csv file.
Add data to a csv file

Resources:
1. https://devenum.com/numpy-savetxt-to-append-to-existing-csv-file/
"""
import numpy as np

class InputExcelFile:

    def __init__(self):
        self.csv_file = open("file.csv", "a")

