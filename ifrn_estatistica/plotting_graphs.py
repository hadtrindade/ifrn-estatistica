from matplotlib import pyplot
from typing import NoReturn, List


class PlottingGraphs:

    """Geração de graficos.

    exemple:

        from ifrn_estatistica.descriptive_table import DescriptiveTable
        from ifrn_estatistica.plotting_graphs import PlottingGraphs


        table = DescriptiveTable(dataset, 3)
        classes = table.classes()
        percentages = table.percentage()
        fci = table.fci()

        plot = PlottingGraphs(dataset, classes, percentages, fci)
        plot.simple_graph()
        plot.histogram_chart()
        plot.histogram_chart_bars()
        plot.pie_chart()
    """

    def __init__(
        self, dataset: List, classes: List, percentages: List, fci: List
    ):
        """Inicia o obj para geração dos gráficos.

        :param dataset: list com os dados para geração de histograma
        :param classes: lista com os nomes das classes
        :param percentages: lista com as porcentagens.
        :param fci: lista com as porcentagens "fci"
        """
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

        :return: None
        """
        name_classes = self._class_names()
        pyplot.hist(self.dataset, bins=len(name_classes), rwidth=0.95)
        pyplot.title("HISTOGRAMA DE FREQUENCIA")
        pyplot.show()

    def simple_graph(self) -> NoReturn:
        """Método para geração de grafico simples.

        :return: None
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

        :return: None
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

        :return: None
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
