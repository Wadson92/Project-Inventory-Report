from xml.etree.ElementTree import parse
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    FILE_EXTENSION = ".xml"

    @classmethod
    def import_data(cls, file_path):
        super().import_data(file_path)
        with open(file_path, "r") as file:
            inventory = []
            for row in parse(file).getroot():
                row_content = {}
                for child in row.getchildren():
                    row_content[child.tag] = child.text
                inventory.append(row_content)
            return inventory
