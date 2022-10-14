import pathlib
import os


class InvalidArgumentException(Exception):

    def __init__(self, str, *args):
        self.str = str

    def __str__(self, str):
        file_extension = pathlib.Path(self.str).suffix
        return f'extention not exists'


def get_path_extension(path: str) -> str:
    try:
        file_extension = pathlib.Path(path).suffix
    except InvalidArgumentException:
        print("No extentions")
    extension = str()
    return file_extension
