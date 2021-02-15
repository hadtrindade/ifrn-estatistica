from ifrn_estatistica.descriptive_table import DescriptiveTable
from ifrn_estatistica.plotting_graphs import PlottingGraphs
from ifrn_estatistica.emparn import Emparn


e = Emparn()
dataset_year, dataset_months = e.data_processing()


t = DescriptiveTable(dataset_year, 3)
classes = t.classes()
porcentagem = t.percentage()
fci = t.fci()

t.generate_table()
p = PlottingGraphs(
    dataset=dataset, classes=classes, percentages=porcentagem, fci=fci
)
p.histogram_chart_bars()
p.pie_chart()
