import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    FILE_EXTENSION = ".json"

    @classmethod
    def import_data(cls, file_path):
        super().import_data(file_path)
        with open(file_path, "r") as file:
            return json.load(file)
