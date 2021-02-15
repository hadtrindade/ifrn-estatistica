from matplotlib import pyplot
from typing import NoReturn, List


class PlottingGraphs:

    """Classe para  geração de graficos.

        Arguments:
            classes: list -- lista com as classes
            percentages: list -- lista com os valores percentuais
            fci: list -- lista com os valores percentuais
        Returns: None
    """

    def __init__(
        self, dataset: List, classes: List, percentages: List, fci: List
    ):
        self.dataset = dataset
        self.classes = classes
        self.percentages = percentages
        self.fci = fci

    def _class_names(self):

        return [
            f"{self.classes[i][0]} |- {self.classes[i][1]}"
            for i in range(len(self.classes))
        ]

    def histogram_chart(self,) -> NoReturn:
        """Método para geração de grafico histograma.
            Return: None
        """
        name_classes = self._class_names()
        pyplot.hist(self.dataset, bins=len(name_classes), rwidth=0.95)
        pyplot.title("HISTOGRAMA DE FREQUENCIA")
        pyplot.show()

    def simple_graph(self) -> NoReturn:
        """Método para geração de grafico simples.
            Return: None
        """
        name_classes = self._class_names()
        pyplot.plot(self.percentages, label="FPI")
        pyplot.plot(self.fci, label="FCI")
        pyplot.xticks(
            range(0, len(self.percentages)),
            name_classes,
            rotation=30,
            size="small",
        )
        pyplot.title("FPI & FCI")
        pyplot.legend()
        pyplot.show()

    def pie_chart(self) -> NoReturn:
        """Método para geração de grafico pizza.
            Return: None
        """
        name_classes = self._class_names()
        pyplot.pie(self.percentages, autopct="%1.1f%%", startangle=90)
        pyplot.title("GRAFICO FPI PIE")
        pyplot.legend(
            name_classes,
            title="Classes",
            loc="center left",
            bbox_to_anchor=(1, 0, 0.5, 1),
        )
        pyplot.show()

    def histogram_chart_bars(self) -> NoReturn:
        """Método para geração de grafico histograma com barras.
            Returns: None
        """
        name_classes = self._class_names()
        pyplot.bar(
            range(0, (len(self.percentages) * 2), 2),
            self.percentages,
            label="%",
        )
        pyplot.bar(range(1, (len(self.fci) * 2), 2), self.fci, label="fci")
        pyplot.xticks(
            range(0, (len(self.percentages) * 2), 2),
            name_classes,
            rotation=30,
            size="small",
        )
        pyplot.title("HISTOGRAMA DA TABELA")
        pyplot.xlabel("Classes")
        pyplot.legend()
        pyplot.ylabel("Porcentagem")
        pyplot.show()
