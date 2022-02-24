from abc import ABC


class Importer(ABC):
    FILE_EXTENSION = "."

    @classmethod
    def import_data(cls, file_path):
        *path, extension = file_path.split(".")
        if f".{extension}" != cls.FILE_EXTENSION:
            raise ValueError("Arquivo inválido")
