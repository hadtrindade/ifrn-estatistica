from ifrn_estatistica.descriptive_table import DescriptiveTable
import pytest

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


@pytest.fixture(scope="module")
def descriptive_table():
    return DescriptiveTable(dataset, 3)


def test_amplitude(descriptive_table):
    assert descriptive_table._amplitude == 13


def test_numero_de_classes_deve_ser_6(descriptive_table):
    assert descriptive_table._number_classes == 6


@pytest.mark.parametrize(
    'value',
    [(22, 35), (35, 48), (48, 61), (61, 74), (74, 87), (87, 100)]
)
def test_classes_da_tabela(descriptive_table, value):
    descriptive_table.generate_classes()
    assert value in descriptive_table._table["Classes"]
