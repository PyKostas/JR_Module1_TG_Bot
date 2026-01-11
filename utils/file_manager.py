import os
from .enum_path import Path

class FileManager:

    def read_txt(path: Path, file_name: str):
        if not file_name.endswith(".txt"):
            file_name += ".txt"
            path = os.path.join(path.value, file_name)
        with open(path, "r") as f:
            return f.read()