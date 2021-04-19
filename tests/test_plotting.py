from unittest.mock import Mock
import pytest
from ifrn_estatistica.descriptive_table import DescriptiveTable
from ifrn_estatistica.plotting_graphs import PlottingGraphs


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


@pytest.fixture
def plotting(mocker):
    respose_mock = Mock()
    respose_mock.show.return_value = None
    get_mock = mocker.patch("ifrn_estatistica.plotting_graphs.pyplot.show")
    get_mock.return_value = respose_mock

    table = DescriptiveTable(dataset=dataset, decimal_places=3)
    classes = table.classes()
    porcentagem = table.percentage()
    fci = table.fci()
    plot = PlottingGraphs(
        dataset=dataset, classes=classes, percentages=porcentagem, fci=fci
    )
    return plot


def test_pie_chart(plotting):
    assert plotting.pie_chart() is None


def test_histogram_chart(plotting):
    assert plotting.histogram_chart() is None


def test_simple_graph(plotting):
    assert plotting.simple_graph() is None


def test_histogram_chart_bars(plotting):
    assert plotting.histogram_chart_bars() is None


def test_normal_distribution_chart(plotting):
    table = DescriptiveTable(dataset=dataset, decimal_places=3)
    mu = table.get_average()
    sigma = table.standard_deviation()
    from math import sqrt

    t = (50 - mu) / (sigma / sqrt(len(dataset)))
    assert plotting.distribution_chart(t, _type="student") is None
