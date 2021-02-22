from pandas import read_csv
from ifrn_estatistica.descriptive_table import DescriptiveTable
from ifrn_estatistica.plotting_graphs import PlottingGraphs


def get_dataset():
    data = read_csv("2021-02-20_accumulated.csv")

    return {k: list(v.values) for k, v in data.items() if k != "Unnamed: 0"}


def gen_table(dict_dataset):

    for k in dict_dataset.keys():
        print(k)
        table = DescriptiveTable(dict_dataset[k], 3)
        classes = table.classes()
        porcentagem = table.percentage()
        fci = table.fci()
        table.generate_table()

        plot = PlottingGraphs(
            dataset=dict_dataset[k],
            classes=classes,
            percentages=porcentagem,
            fci=fci,
        )

        plot.histogram_chart_bars()
        plot.pie_chart()


if __name__ == "__main__":
    datasets = get_dataset()
    gen_table(datasets)
