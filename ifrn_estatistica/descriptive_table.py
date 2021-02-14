from typing import List, Dict
from math import log
from tabulate import tabulate 


class DescriptiveTable:

    def __init__(self, dataset: List, decimal_places: int, *args, **kwargs):

        self.dataset = dataset
        self.decimal_places = decimal_places
        self._table = {}
        self._number_classes = self.sturges_rule()
        self._amplitude = self.amplitude_classes()

    def amplitude_classes(self) -> int:
        """Método para retornar a amplitude de classes.
            Return:
            int - aplitude de classes
        """

        at = max(self.dataset) - min(self.dataset)
        return round(at / self._number_classes)

    def sturges_rule(self) -> int:

        """Método para retornar a numero de classes.
            Return:
            int - numero de classes
        """
        return round(1 + 3.322 * log(len(self.dataset), 10))

    def generate_classes(self) -> Dict:
        """Método para geração das classes da tabela descritiva.

        Return:
            dict -- lista com as classes
        """
        limite_inferior = min(self.dataset)
        classes = []
        for i in range(1, self._number_classes+1):
            classes.append((
                round(limite_inferior, self.decimal_places),
                round(
                    (limite_inferior + self._amplitude), self.decimal_places
                    )),
                    )
            limite_inferior += self._amplitude
        self._table["Classes"] = classes
        return classes

    def generate_table(self):

        print(tabulate(self._table, headers="keys", tablefmt="fancy_grid"))

    def __repr__(self):
        return "Classe Tabela descritiva"
