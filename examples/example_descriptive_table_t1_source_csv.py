from pandas import read_csv
from ifrn_estatistica.descriptive_table import DescriptiveTable
from ifrn_estatistica.plotting_graphs import PlottingGraphs


def get_dataset():
    data = read_csv("2021-04-14_accumulated.csv")

    return {k: list(v.values) for k, v in data.items() if k != "Unnamed: 0"}


def gen_table(dict_dataset):

    for k in dict_dataset.keys():
        print(k)
        table = DescriptiveTable(dataset=dict_dataset[k], decimal_places=3)
        classes = table.classes()
        table.simple_frequency()
        table.cumulative_frequency()
        table.simple_relative_frequency()
        table.cumulative_relative_frequency()
        table.middle_point()
        mu = table.get_average()
        porcentagem = table.percentage()
        fci = table.fci()
        table.angle()
        table.deviation()
        table.deviation_v1()
        table.deviation_v2()
        table.get_moda()
        table.get_varience()
        table.get_median()
        sigma = table.standard_deviation()
        table.generate_table()
        from math import sqrt

        t1 = (100 - mu) / (sigma / sqrt(len(table.dataset)))
        t2 = (1700 - mu) / (sigma / sqrt(len(table.dataset)))

        plot = PlottingGraphs(
            dataset=dict_dataset[k],
            classes=classes,
            percentages=porcentagem,
            fci=fci,
        )

        plot.histogram_chart_bars()
        plot.histogram_chart()
        plot.pie_chart()
        plot.distribution_chart(
            title=k,
            value1=t1,
            value2=t2,
            df=len(table.dataset),
            _type="student",
        )


if __name__ == "__main__":
    datasets = get_dataset()
    gen_table(datasets)
