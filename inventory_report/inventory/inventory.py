from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def import_data(file_path, report_type):
        inventory = []
        if file_path.endswith("csv"):
            inventory = CsvImporter.import_data(file_path)
        elif file_path.endswith("json"):
            inventory = JsonImporter.import_data(file_path)
        elif file_path.endswith("xml"):
            inventory = XmlImporter.import_data(file_path)
        else:
            raise ValueError("Tipo de arquivo não aceito")

        if report_type == "simples":
            return SimpleReport.generate(inventory)
        return CompleteReport.generate(inventory)
