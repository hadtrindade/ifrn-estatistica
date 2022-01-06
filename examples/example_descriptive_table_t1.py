from datetime import datetime

from ifrn_estatistica.descriptive_table import DescriptiveTable
from ifrn_estatistica.emparn import (accumulated_annual_rainfall,
                                     get_city_stations)
from ifrn_estatistica.plotting_graphs import PlottingGraphs


def gen_table(name, dataset):

    print(name)
    table = DescriptiveTable(dataset, 3)
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
        dataset=dataset,
        classes=classes,
        percentages=porcentagem,
        fci=fci,
    )

    plot.histogram_chart_bars()
    plot.histogram_chart()
    plot.pie_chart()


if __name__ == "__main__":

    city_stations = get_city_stations()

    dataset = accumulated_annual_rainfall(
        places=[city_stations["Natal"][1]],
        start_day=datetime(1992, 1, 1).isoformat() + "-03:00",
        final_day=datetime(2022, 1, 1).isoformat() + "-03:00",
    )
    gen_table(name="Natal", dataset=dataset)
