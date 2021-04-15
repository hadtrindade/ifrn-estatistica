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
    "value", [(22, 35), (35, 48), (48, 61), (61, 74), (74, 87), (87, 100)]
)
def test_classes_da_tabela(descriptive_table, value):
    descriptive_table.classes()
    assert value in descriptive_table._table["Classes"]


@pytest.mark.parametrize("value", [5, 3, 6, 10, 5, 6])
def test_frenquencia_simples(descriptive_table, value):
    descriptive_table.simple_frequency()
    assert value in descriptive_table._table["fi"]


@pytest.mark.parametrize("value", [5, 8, 14, 24, 29, 35])
def test_frenquencia_acumulada(descriptive_table, value):
    descriptive_table.cumulative_frequency()
    assert value in descriptive_table._table["Fi"]


@pytest.mark.parametrize("value", [0.143, 0.086, 0.171, 0.286, 0.143, 0.171])
def test_frequencia_relativa_simples(descriptive_table, value):
    descriptive_table.simple_relative_frequency()
    assert value in descriptive_table._table["fri"]


@pytest.mark.parametrize("value", [0.143, 0.229, 0.4, 0.686, 0.829, 1.0])
def test_frequencia_relativa_acumulada(descriptive_table, value):
    descriptive_table.cumulative_relative_frequency()
    assert value in descriptive_table._table["Fri"]


@pytest.mark.parametrize("value", [28.5, 41.5, 54.5, 67.5, 80.5, 93.5])
def test_ponto_medio(descriptive_table, value):
    descriptive_table.middle_point()
    assert value in descriptive_table._table["XI"]


@pytest.mark.parametrize("value", [14.3, 8.6, 17.1, 28.6, 14.3, 17.1])
def test_percentual(descriptive_table, value):
    descriptive_table.percentage()
    assert value in descriptive_table._table["%"]


@pytest.mark.parametrize("value", [51.48, 82.44, 144.0, 246.96, 298.44, 360.0])
def test_angulo(descriptive_table, value):
    descriptive_table.angle()
    assert value in descriptive_table._table["Ang"]


@pytest.mark.parametrize("value", [35.286, 22.286, 9.286, 3.714, 16.714, 29.714])
def test_valor_de_desvio_devem_ser_(descriptive_table, value):
    assert value in descriptive_table.deviation()


@pytest.mark.parametrize("value", [1245.102, 496.666, 86.23, 13.794, 279.358, 882.922])
def test_valores_de_v1_devem_ser_(descriptive_table, value):
    assert value in descriptive_table.deviation_v1()


@pytest.mark.parametrize(
    "value", [6225.51, 1489.998, 517.38, 137.94, 1396.79, 5297.532]
)
def test_valor_de_v2_devem_ser_(descriptive_table, value):
    assert value in descriptive_table.deviation_v2()


def test_valor_da_varianca_de_ser_443_093(descriptive_table):
    assert descriptive_table.get_varience() == 443.093


def test_valor_do_desvio_padrao_de_ser_21_05(descriptive_table):
    assert descriptive_table.standard_deviation() == 21.05


@pytest.mark.parametrize("value", [3.25, 4.25, 6.25, 7.75, 6.5, 4.25])
def test_valor_de_fci_devem_ser_(descriptive_table, value):
    assert value in descriptive_table.fci()


@pytest.mark.parametrize("value", [142.5, 124.5, 327.0, 675.0, 402.5, 561.0])
def test_valor_de_xifi_de_ser_(descriptive_table, value):
    assert value in descriptive_table.weighted_average()


def test_valor_da_media_deve_ser_63_786(descriptive_table):
    assert descriptive_table.get_average() == 63.786


def test_valor_da_mediana_deve_ser_65(descriptive_table):
    assert descriptive_table.get_median() == 65.55


def test_valor_da_moda_deve_ser_64_714(descriptive_table):
    assert descriptive_table.get_moda() == 64.714
