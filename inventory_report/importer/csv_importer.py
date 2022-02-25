import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    FILE_EXTENSION = ".csv"

    @classmethod
    def import_data(cls, file_path):
        super().import_data(file_path)
        with open(file_path, "r") as file:
            inventory = csv.DictReader(file, delimiter=",", quotechar="\"")
            return[*inventory]
