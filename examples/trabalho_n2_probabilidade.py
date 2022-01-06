from math import sqrt

from pandas import read_csv
from scipy import stats

from ifrn_estatistica.descriptive_table import DescriptiveTable
from ifrn_estatistica.plotting_graphs import PlottingGraphs


def get_dataset():
    data = read_csv("2021-04-14_accumulated.csv")

    return {k: list(v.values) for k, v in data.items() if k != "Unnamed: 0"}


def intervalo_de_confianca(numero_amostras, interval):
    """Calcula o intervalo de confiança."""
    return stats.t.interval(interval, df=numero_amostras)


def probabilidade_dado_um_valor(
    numero_amostras, x, mu=0, sigma=1, df=10000000
):
    """Calcula a probabilidade dado um valor."""

    t1 = (x - mu) / (sigma / sqrt(numero_amostras))
    p_t1 = stats.t(df=df, loc=0, scale=1).cdf(t1)
    return t1, p_t1


def probabilidade_dado_um_intervalo(
    numero_amostras, x1, x2, mu=0, sigma=1, df=10000000
):
    """Calcula a probabilidade dado um intervalo de valores."""

    t1 = (x1 - mu) / (sigma / sqrt(numero_amostras))
    t2 = (x2 - mu) / (sigma / sqrt(numero_amostras))
    p_t1 = stats.t(df=df, loc=0, scale=1).cdf(t1)
    p_t2 = stats.t(df=df, loc=0, scale=1).cdf(t2)
    probabilidade = p_t2 - p_t1

    return t1, t2, probabilidade


def probabilidade_t_score(t, df=10000000):
    """Calcula a probabilidade dado um t score."""

    p_t1 = stats.t(df=df, loc=0, scale=1).cdf(t)
    return p_t1


def probabilidade_dado_uma_cdf(percentage, mu=0, sigma=1, df=10000000):
    """Dado uma probrabilidade calcula o valor."""
    t = round(stats.t.ppf(percentage, df=df, loc=0, scale=1), 3)
    x = mu + t * sigma
    return t, x


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

        # plot.histogram_chart_bars()
        # plot.histogram_chart()
        # plot.pie_chart()

        t1, probabilidade = probabilidade_dado_um_valor(
            len(table.dataset),
            x=600,
            mu=mu,
            sigma=sigma,
            df=len(table.dataset) - 1,
        )

        margem_de_erro = round(
            intervalo_de_confianca(len(table.dataset) - 1, 0.95)[1], 3
        )
        print(f"Margem de erro para mais ou para menos: {margem_de_erro} ")
        print(
            f"Probabilidade de chover acima de 600mm em {k} é {round((1 - probabilidade)*100, 3)}%"
        )
        plot.distribution_chart(
            title=k,
            value1=t1,
            df=len(table.dataset) - 1,
            _type="student",
        )

        t1, t2, probabilidade = probabilidade_dado_um_intervalo(
            numero_amostras=len(table.dataset),
            x1=700,
            x2=1200,
            mu=mu,
            sigma=sigma,
            df=len(table.dataset) - 1,
        )
        print(
            f"Qual a probabilidade de chover entre 700 e 1200mm na cidade de {k}? {round(probabilidade*100, 3)}%"
        )
        plot.distribution_chart(
            title=k,
            value1=t1,
            value2=t2,
            df=len(table.dataset) - 1,
            _type="student",
        )

        if k == "PAU DOS FERROS":
            print(
                f"Dado a probabilidade de 85%, qual a quantidade de chuva em milimetros que esse valor representa na cidade de {k}."
            )
            t, x = probabilidade_dado_uma_cdf(
                0.85, mu=mu, sigma=sigma, df=len(table.dataset) - 1
            )
            probabilidade = probabilidade_t_score(
                t=t, df=len(table.dataset) - 1
            )
            print(f"Milimetros para 85% é: {round(x, 3)}mm")
            print(
                f"Percentual para {round(x, 3)}mm é: {round(probabilidade*100, 3)}%"
            )
            plot.distribution_chart(
                title=k,
                value2=t,
                df=len(table.dataset) - 1,
                _type="student",
            )


if __name__ == "__main__":
    datasets = get_dataset()
    gen_table(datasets)
