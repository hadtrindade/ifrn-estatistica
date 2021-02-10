from typing import List, Dict
from math import log


dataset = [
    70,
    99,
    36,
    27,
    81,
    61,
    72,
    26,
    56,
    98,
    26,
    33,
    92,
    73,
    45,
    42,
    97,
    48,
    99,
    93,
    49,
    80,
    22,
    58,
    75,
    49,
    74,
    67,
    72,
    71,
    73,
    82,
    52,
    62,
    72,
]


class DescriptiveTable:
    def __init__(self, dataset: List, decimal_places: int, *args, **kwargs):

        self.dataset = dataset
        self.decimal_places = decimal_places
        self._number_classes = self.sturges_rule()
        self._amplitude = self.amplitude_classes()
        self._classes = self.generate_classes()

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
        classes = {}
        for i in range(1, self._number_classes+1):
            classes[i] = (
                round(limite_inferior, self.decimal_places),
                round(
                    (limite_inferior + self._amplitude), self.decimal_places
                    ),
                    )
            limite_inferior += self._amplitude
        return classes

    def __repr__(self):
        return "Classe Tabela descritiva"


if __name__ == "__main__":
    table = DescriptiveTable(dataset, 3)
    print(
        f"Aplitude: {table._amplitude}, "
        f"Némero de classes: {table._number_classes} e "
        f"classes: {table._classes}"
    )
