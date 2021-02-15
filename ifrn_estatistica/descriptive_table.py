from typing import List
from math import log, sqrt
from tabulate import tabulate


class DescriptiveTable:
    def __init__(self, dataset: List, decimal_places: int):

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

    def fci(self) -> List:
        """Método para geração de valores para grafico suavisado.

            Return:
            list -- valores do grafico suavisado.
        """
        fi = self.simple_frequency()
        fci = list()
        for i in range(self._number_classes):
            if i == 0:
                fci.append(((2 * fi[i]) + fi[(i + 1)]) / 4)
            else:
                try:
                    fci.append(((fi[(i - 1)] + (2 * fi[i]) + fi[(i + 1)]) / 4))
                except IndexError:
                    fci.append((fi[(i - 1)] + 2 * fi[i]) / 4)
        self._table["FCI"] = fci
        return fci

    def weighted_average(self):
        """Método para retorno de XIFI.

        Return:
            list -- lista com os valores de XIFI
        """
        xi = self.middle_point()
        fi = self.simple_frequency()
        xifi = list()
        for i in range(self._number_classes):
            xifi.append(round(xi[i] * fi[i], self.decimal_places))
        self._table["XIFI"] = xifi
        return xifi

    def v0(self) -> float:
        """Método para geração de V0.
            Returns:
            float -- v0 value.
        """
        xi = self.middle_point()
        fi = self.simple_frequency()
        v0 = list()
        for i in range(len(xi)):
            v0.append(round(abs((xi[i] - fi[i])), self.decimal_places))
        self._table["V0"] = v0
        return v0

    def v1(self) -> float:
        """Método para geração de V1
        Return:
            v1 -- v1 value
        """
        xi = self.middle_point()
        fi = self.simple_frequency()
        v1 = list()
        for i in range(len(xi)):
            v1.append(round(abs((xi[i] - fi[i])) * fi[i], self.decimal_places))
        self._table["V1"] = v1
        return v1

    def v2(self) -> float:
        """Método para o retorno de V2
            Return:
                float -- value v2
        """
        xi = self.middle_point()
        fi = self.simple_frequency()
        v2 = list()
        for i in range(len(xi)):
            v2.append(
                round(abs((xi[i] - fi[i])) ** 2 * fi[i], self.decimal_places)
            )
        self._table["V2"] = v2
        return v2

    def get_varience(self):
        """Método para geração da variancia.
            Returns:
                float -- valor da variancia.
        """
        sum_v2 = sum(self.v2())
        variancia = round(
            (sum_v2 / (len(self.dataset) - 1)), self.decimal_places
        )
        self._table["Variancia"] = [round(variancia, self.decimal_places)]
        return round(variancia, self.decimal_places)

    def standard_deviation(self) -> float:
        """Método para geração do desvio padrão.

        Returns:
            float -- valor do desvio padrão.
        """
        variance = self.get_varience()
        std_dev = round(sqrt(variance), self.decimal_places)
        self._table["Desvio Padrão"] = [std_dev]
        return std_dev

    def get_average(self) -> float:
        """Método para calculara média.
            Return:
            float -- valor da média.
        """
        xifi = self.weighted_average()
        average = round(sum(xifi) / len(self.dataset), self.decimal_places)
        self._table["Media"] = [average]
        return average

    def get_moda(self) -> float:
        """Método para geração da moda.
            Returns:
                float -- valor da moda
        """
        classes = self.classes()
        avarege = self.get_average()
        fi = self.simple_frequency()
        for cm in range(self._number_classes):
            if avarege >= classes[cm][0] and avarege < classes[cm][1]:
                if cm == 0:
                    moda = round(
                        classes[cm][0]
                        + ((fi[cm]) / ((2 * fi[cm]) - fi[(cm + 1)]))
                        * self._amplitude,
                        self.decimal_places,
                    )
                else:
                    try:
                        moda = round(
                            classes[cm][0]
                            + (
                                (fi[cm] - fi[(cm - 1)])
                                / (
                                    (2 * fi[cm])
                                    - (fi[(cm - 1)] + fi[(cm + 1)])
                                )
                            )
                            * self._amplitude,
                            self.decimal_places,
                        )
                    except IndexError:
                        moda = round(
                            classes[cm][0]
                            + (
                                (fi[cm] - fi[(cm - 1)])
                                / ((2 * fi[cm]) - (fi[(cm - 1)]))
                            )
                            * self._amplitude,
                            self.decimal_places,
                        )
        self._table["MODA"] = [moda]
        return round(moda, self.decimal_places)

    def get_median(self):
        """Método para geração de médiana
            Return:
                float -- valor da mediana
        """
        classes = self.classes()
        fi = self.simple_frequency()
        h = self._amplitude
        Fi = self.cumulative_frequency()
        cmd = sum(fi) / 2
        median = 0
        for icmd in range(len(Fi)):
            if icmd == 0:
                if 0 <= cmd <= Fi[icmd]:
                    median = classes[icmd][0] + ((cmd / fi[icmd]) * h)
            if Fi[(icmd - 1)] <= cmd <= Fi[icmd]:
                median = classes[icmd][0] + (
                    ((cmd - Fi[(icmd - 1)]) / fi[icmd]) * h
                )
        self._table["Mediana"] = [round(median, self.decimal_places)]
        return round(median, self.decimal_places)

    def generate_table(self):
        self.classes()
        self.simple_frequency()
        self.cumulative_frequency()
        self.simple_relative_frequency()
        self.cumulative_relative_frequency()
        self.middle_point()
        self.percentage()
        self.angle()
        self.v0()
        self.v1()
        self.v2()
        self.get_moda()
        self.get_varience()
        self.get_median()
        print(tabulate(self._table, headers="keys", tablefmt="fancy_grid"))

    def __repr__(self):
        return "Classe Tabela descritiva"
