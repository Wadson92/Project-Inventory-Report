from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(self):
        next_date = datetime.now().isoformat()
        old_date = self[0]["data_de_fabricacao"]
        valid_date = self[0]["data_de_validade"]
        company = {}
        for data in self:
            if data["data_de_fabricacao"] <= old_date:
                old_date = data["data_de_fabricacao"]
            if next_date <= data["data_de_validade"] <= valid_date:
                valid_date = data["data_de_validade"]
            if data["nome_da_empresa"] not in company:
                company[data["nome_da_empresa"]] = 1
            else:
                company[data["nome_da_empresa"]] += 1

        return (
            f'Data de fabricação mais antiga: {old_date}\n'
            f'Data de validade mais próxima: {valid_date}\n'
            f'Empresa com maior quantidade de produtos '
            f'estocados: {max(company)}\n'
        )
