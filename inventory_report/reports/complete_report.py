from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(data):
        simple_report = SimpleReport.generate(data)
        prod_quant = {}
        print(simple_report)
        inventory = ""
        for product in data:
            if product["nome_da_empresa"] in prod_quant:
                prod_quant[product["nome_da_empresa"]] += 1
            else:
                prod_quant[product["nome_da_empresa"]] = 1
        for product in prod_quant.keys():
            inventory = f"{inventory}- {product}: {prod_quant[product]}\n"
        return (
            f'{simple_report}'
            f'\nProdutos estocados por empresa: \n'
            f'{inventory}'
        )
