# Utils

from .exceptions import RossWriteFileException


def write_file(filename: str, data: str, mode="w"):
    try:
        with open(filename, mode) as f:
            f.write(data)
        return True
    except Exception as e:
        raise RossWriteFileException(e)
