from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """

    with open(path) as file:
        data = csv.DictReader(file)
        content = []
        for row in data:
            content.append(row)

    return content
