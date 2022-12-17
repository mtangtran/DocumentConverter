import filecmp
import os


def file_comparison(file1, file2):
    """
    Returns a comparison for two different files.
    True if it is the same. Else it is false.

    :param file1:
    :param file2:
    :return:
    """
    result = filecmp.cmp(file1, file2)
    if result == 0:
        return True
    else:
        return False


def getFileSize(filename):
    """
    Get the size of the file.
    :param filename:
    :return:
    """
    os.path.getsize(filename)


def getFileSizeComparison(file1, file2):
    """
    Compares the two inputted files and then returns a string on the relative size comparison.
    :param file1:
    :param file2:
    :return:
    """
    file1_size = os.path.getsize(file1)
    file2_size = os.path.getsize(file2)

    if file1_size > file2_size:
        return "{} is larger than {}".format(file1, file2)
    elif file1_size == file2_size:
        return "They are the same size"
    elif file1_size < file2_size:
        return "{} is smaller than {}".format(file1, file2)
