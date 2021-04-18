from typing import NoReturn, List
from typing import Union
from matplotlib import pyplot
from scipy.stats import norm
import numpy as np


numeric = Union[int, float, complex]


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
        plot.normal_curve()
    """

    def __init__(
        self,
        dataset: List,
        classes: List,
        percentages: List,
        fci: List,
        keep: bool = None,
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
        self.keep = keep

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
        if self.keep:
            pyplot.savefig("histogram_chart.png")
        else:
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
        if self.keep:
            pyplot.savefig("simple_graph.png")
        else:
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
        if self.keep:
            pyplot.savefig("pie_chart.png")
        else:
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
        if self.keep:
            pyplot.savefig("histogram_table.png")
        else:
            pyplot.show()

    def distribution_chart(
        self, title="", z1: numeric = 0, z2: numeric = 0,
    ) -> NoReturn:

        x = np.arange(z1, z2, 0.001)
        x_normal_curve = np.arange(-10, 10, 0.001)
        y_probility = norm.pdf(x, 0, 1)
        y_normal_curve = norm.pdf(x_normal_curve, 0, 1)
        _, ax = pyplot.subplots(figsize=(9, 6))
        pyplot.style.use("fivethirtyeight")
        ax.plot(x_normal_curve, y_normal_curve)
        ax.fill_between(x, y_probility, 0, alpha=0.3, color="b")
        ax.fill_between(x_normal_curve, y_normal_curve, 0, alpha=0.1)
        ax.set_xlim([-4, 4])
        ax.set_xlabel("Desvio Padrão")
        ax.set_yticklabels([])
        ax.set_title(f"Distribuição Normal para {title}")
        pyplot.legend(
            [],
            title="Medidas de Dispersão",
            loc="upper right",
            #bbox_to_anchor=(1, 0, 0.5, 1),
        )

        if self.keep:
            pyplot.savefig("normal_curve.png", dpi=72, bbox_inches="tight")
        else:
            pyplot.show()
