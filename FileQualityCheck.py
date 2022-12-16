import filecmp


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
