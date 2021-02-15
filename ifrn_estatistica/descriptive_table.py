from typing import List
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

    def classes(self) -> List:
        """Método para geração das classes da tabela descritiva.

        Return:
            list -- lista com as classes
        """
        limite_inferior = min(self.dataset)
        classes = []
        for i in range(1, self._number_classes + 1):
            classes.append(
                (
                    round(limite_inferior, self.decimal_places),
                    round(
                        (limite_inferior + self._amplitude),
                        self.decimal_places,
                    ),
                ),
            )
            limite_inferior += self._amplitude
        self._table["Classes"] = classes
        return classes

    def simple_frequency(self) -> List:
        """Método para geração do frequencia simples "fi".

            Return:
                list - lista com as classes
        """
        classes = self.classes()
        fi = list()
        count_fi = 0
        for i in range(self._number_classes):
            for j in range(len(self.dataset)):
                if (
                    self.dataset[j] >= classes[i][0]
                    and self.dataset[j] < classes[i][1]
                ):
                    count_fi += 1
            fi.append(count_fi)
            count_fi = 0
        self._table["fi"] = fi
        return fi

    def cumulative_frequency(self) -> List:
        """Método para geranção a frequencia acumulada.

            Returns:
            list -- lista com a frequencia acumulada
        """
        fi = self.simple_frequency()
        Fi = list()
        for i in range(self._number_classes):
            if i == 0:
                Fi.append(fi[i])
            else:
                Fi.append((Fi[-1] + fi[i]))
        self._table["Fi"] = Fi
        return Fi

    def simple_relative_frequency(self) -> List:
        """Método para geração da frequencia relativa simples "fri".
            Return:
                list -- list com a frequencia relativa simples.
        """
        fi = self.simple_frequency()
        fri = list()
        for i in range(self._number_classes):
            if i == 0:
                fri.append(
                    (round(fi[i] / len(self.dataset), self.decimal_places))
                )
            else:
                fri.append(
                    (round(fi[i] / len(self.dataset), self.decimal_places))
                )
        self._table["fri"] = fri
        return fri

    def cumulative_relative_frequency(self) -> List:

        """Método para retorno da frenquencia relativa acumulada "Fri".


            Returns:
                [list] -- lista com os valores da frenquancia relativa acumulada.
        """
        fi = self.simple_frequency()
        fri = self.simple_relative_frequency()
        Fri = list()
        for i in range(self._number_classes):
            if i == 0:
                Fri.append(
                    (round(fi[i] / len(self.dataset), self.decimal_places))
                )
            else:
                Fri.append((round((fri[i] + Fri[-1]), self.decimal_places)))
        self._table["Fri"] = Fri
        return Fri

    def middle_point(self) -> List:
        """Método para geração dos pontos médios.

            Returns:
            list -- lista com os pontos médios.
        """
        classes = self.classes()
        xi = list()
        for i in range(self._number_classes):
            xi.append(
                round((classes[i][0] + classes[i][1]) / 2, self.decimal_places)
            )
        self._table["XI"] = xi
        return xi

    def percentage(self) -> List:
        """Método para geração do percentual "%".

            Returns:
                list -- lista com os valores do percentual
        """
        fri = self.simple_relative_frequency()
        percentage_values = list()
        for i in range(self._number_classes):
            if i == 0:
                percentage_values.append(
                    (round((fri[i] * 100), self.decimal_places))
                )
            else:
                percentage_values.append(
                    (round((fri[i] * 100), self.decimal_places))
                )
        self._table["%"] = percentage_values
        return percentage_values

    def angle(self) -> List:
        """Método para geração dos angulos "Ang".

            Returns:
                [list] -- lista com as valores dos angulos
        """
        Fri = self.cumulative_relative_frequency()
        angle_values = list()
        for i in range(self._number_classes):
            if i == 0:
                angle_values.append(round((Fri[i] * 360), self.decimal_places))
            else:
                angle_values.append(round((Fri[i] * 360), self.decimal_places))
        self._table["Ang"] = angle_values
        return angle_values

    def generate_table(self):

        print(tabulate(self._table, headers="keys", tablefmt="fancy_grid"))

    def __repr__(self):
        return "Classe Tabela descritiva"
