from math import sqrt
from pandas import read_csv
from ifrn_estatistica.descriptive_table import DescriptiveTable
from ifrn_estatistica.plotting_graphs import PlottingGraphs
from scipy import stats


def get_dataset():
    data = read_csv(
        "/home/hadd/sync/ifrn-estatistica/2021-04-14_accumulated.csv"
    )

    return {k: list(v.values) for k, v in data.items() if k != "Unnamed: 0"}


def intervalo_de_confianca(dataset):
    """Calcula o intervalo de confiança."""
    return stats.t.interval(0.95, df=len(dataset))


def probabilidade_dado_um_valor(dataset, x, mu=0, sigma=1, df=10000000):
    """Calcula a probabilidade dado um valor."""

    t1 = (x - mu)/(sigma/sqrt(len(dataset)))
    p_t1 = stats.t(df=df, loc=0, scale=1).cdf(t1)
    return p_t1


def probabilidade_dado_um_intervalo(dataset, x1, x2, mu=0, sigma=1, df=10000000):
    """Calcula a probabilidade dado um intervalo de valores."""

    t1 = (x1 - mu)/(sigma/sqrt(len(dataset)))
    t2 = (x2 - mu)/(sigma/sqrt(len(dataset)))
    p_t1 = stats.t(df=df, loc=0, scale=1).cdf(t1)
    p_t2 = stats.t(df=df, loc=0, scale=1).cdf(t2)
    probabilidade = p_t2 - p_t1

    return t1, t2, probabilidade


def probabilidade_dado_uma_cdf(percentage, mu=0, sigma=1, df=10000000):
    """Dado uma probrabilidade calcula o valor."""
    z = round(stats.t.ppf(percentage, df=df, loc=0, scale=1), 3)
    x = mu + z*sigma
    return x


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
        

        

        plot = PlottingGraphs(
            dataset=dict_dataset[k],
            classes=classes,
            percentages=porcentagem,
            fci=fci,
        )

        #plot.histogram_chart_bars()
        #plot.histogram_chart()
        #plot.pie_chart()
        plot.distribution_chart(title=k, value1=t1, value2=t2, df=len(table.dataset), _type="student")
        break


if __name__ == "__main__":
    datasets = get_dataset()
    gen_table(datasets)
