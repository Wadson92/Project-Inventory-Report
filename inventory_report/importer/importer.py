from abc import ABC


class Importer(ABC):
    FILE_EXTENSION = "."

    @classmethod
    def import_data(cls, file_path):
        if not file_path.endswith(cls.FILE_EXTENSION):
            raise ValueError("Arquivo inválido")
