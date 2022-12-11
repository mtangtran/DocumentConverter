"""
Add data to a csv file
"""
import numpy as np

class InputExcelFile:

    def __init__(self):
        self.csv_file = open("file.csv", "a")

    