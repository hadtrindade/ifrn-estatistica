from ifrn_estatistica.descriptive_table import DescriptiveTable
from ifrn_estatistica.plotting_graphs import PlottingGraphs
from ifrn_estatistica.emparn import Emparn

dataset = [
    70,
    99,
    36,
    27,
    81,
    61,
    72,
    26,
    56,
    98,
    26,
    33,
    92,
    73,
    45,
    42,
    97,
    48,
    99,
    93,
    49,
    80,
    22,
    58,
    75,
    49,
    74,
    67,
    72,
    71,
    73,
    82,
    52,
    62,
    72,
]
"""
e = Emparn()
dataset_year, dataset_months = e.data_processing()"""


t = DescriptiveTable(dataset, 3)
classes = t.classes()
porcentagem = t.percentage()
fci = t.fci()

t.generate_table()
p = PlottingGraphs(
    dataset=dataset, classes=classes, percentages=porcentagem, fci=fci
)
#p.histogram_chart_bars()
#p.pie_chart()
