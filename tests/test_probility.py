import pytest
from ifrn_estatistica.descriptive_table import DescriptiveTable
from ifrn_estatistica.probability import Probability


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
def probability():
    table = DescriptiveTable(dataset=dataset, decimal_places=3)
    mu = table.get_average()
    sigma = table.standard_deviation()
    prob = Probability(x1=50, x2=74, mu=mu, sigma=sigma)
    return prob


@pytest.mark.parametrize("value", [-0.6549168646080761, 0.48522565320665073])
def test_normalize(probability, value):
    assert value in probability.normalize()


def test_calculate_probability(probability):
    assert probability.calculate_probability() == 43.027
