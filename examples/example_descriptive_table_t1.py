from ifrn_estatistica.descriptive_table import DescriptiveTable
from ifrn_estatistica.plotting_graphs import PlottingGraphs
from ifrn_estatistica.emparn import Emparn


def get_dataset_scraping():

    emparn = Emparn(
        ["NATAL", "MOSSORO", "CAICO", "ASSU"], starting_year=1992, keep=True
    )

    _, datasets = emparn.get_city_data()
    raw_dataset = emparn.raw_city_data()
    return datasets, raw_dataset


def gen_table(datasets):

    dict_dataset = {
        "NATAL": [float(v) for v in datasets["NATAL"].values()],
        "MOSSORO": [float(v) for v in datasets["MOSSORO"].values()],
        "CAICO": [float(v) for v in datasets["CAICO"].values()],
        "ASSU": [float(v) for v in datasets["ASSU"].values()],
    }

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
    datasets, _ = get_dataset_scraping()
    gen_table(datasets)
