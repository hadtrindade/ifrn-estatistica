from ifrn_estatistica.descriptive_table import DescriptiveTable
from ifrn_estatistica.emparn_old_site import Emparn
from ifrn_estatistica.plotting_graphs import PlottingGraphs


def get_dataset_scraping():

    emparn = Emparn(
        ["NATAL", "MOSSORO", "CAICO", "ASSU", "PAU DOS FERROS"], keep=True
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
        "PAU DOS FERROS": [
            float(v) for v in datasets["PAU DOS FERROS"].values()
        ],
    }

    for k in dict_dataset.keys():
        print(k)
        table = DescriptiveTable(dict_dataset[k], 3)
        classes = table.classes()
        table.simple_frequency()
        table.cumulative_frequency()
        table.simple_relative_frequency()
        table.cumulative_relative_frequency()
        table.middle_point()
        porcentagem = table.percentage()
        fci = table.fci()
        table.angle()
        table.deviation()
        table.deviation_v1()
        table.deviation_v2()
        table.get_moda()
        table.get_varience()
        table.get_median()
        table.standard_deviation()
        table.generate_table()

        plot = PlottingGraphs(
            dataset=dict_dataset[k],
            classes=classes,
            percentages=porcentagem,
            fci=fci,
        )

        plot.histogram_chart_bars()
        plot.histogram_chart()
        plot.pie_chart()


if __name__ == "__main__":
    datasets, _ = get_dataset_scraping()
    gen_table(datasets)
