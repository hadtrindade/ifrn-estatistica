import pytest
from unittest.mock import AsyncMock
from ifrn_estatistica.emparn import Emparn


class Data:
    content = """<td class="king" onmouseover="this.bgColor=&#39;#ADD8E6&#39;" onmouseout="this.bgColor=&#39;white&#39;" bgcolor="white" data-darkreader-inline-bgcolor="" style="--darkreader-inline-bgcolor:#181a1b;">NATAL(NATAL-UFRN)</td><td class="king" onmouseover="this.bgColor=&#39;#ADD8E6&#39;" onmouseout="this.bgColor=&#39;white&#39;" bgcolor="white" data-darkreader-inline-bgcolor="" style="--darkreader-inline-bgcolor:#181a1b;">2161.2</td><td class="king" onmouseover="this.bgColor=&#39;#ADD8E6&#39;" onmouseout="this.bgColor=&#39;white&#39;" bgcolor="white" data-darkreader-inline-bgcolor="" style="--darkreader-inline-bgcolor:#181a1b;"><a href="./graficos/q8101.htm">quantis/ano</a></td><td class="king" onmouseover="this.bgColor=&#39;#ADD8E6&#39;" onmouseout="this.bgColor=&#39;white&#39;" bgcolor="white" data-darkreader-inline-bgcolor="" style="--darkreader-inline-bgcolor:#181a1b;"><a href="./graficos/qmes8101.htm">quantis/mes</a></td><td class="king" onmouseover="this.bgColor=&#39;#ADD8E6&#39;" onmouseout="this.bgColor=&#39;white&#39;" bgcolor="white" data-darkreader-inline-bgcolor="" style="--darkreader-inline-bgcolor:#181a1b;"><a href="./graficos/f8101.htm">freq</a></td><td class="king" onmouseover="this.bgColor=&#39;#ADD8E6&#39;" onmouseout="this.bgColor=&#39;white&#39;" bgcolor="white" data-darkreader-inline-bgcolor="" style="--darkreader-inline-bgcolor:#181a1b;"><a href="./graficos/d8101.html">dados</a></td></tr>"""


@pytest.fixture
def emparn(mocker):
    d = Data()
    async_mock = AsyncMock(return_value=[d])
    mocker.patch("ifrn_estatistica.emparn.get_dataset", side_effect=async_mock)

    e = Emparn(["NATAL"], starting_year=2020, keep=True)
    return e


@pytest.mark.parametrize(
    "value",
    [
        {
            "NATAL": [
                "http://meteorologia.emparn.rn.gov.br:8181/monitoramento/2020/graficos/d8101.html"
            ]
        },
        {"NATAL": {2020: 2161.2}},
    ],
)
def test_get_city_data(emparn, value):
    assert value in emparn.get_city_data()


def test_get_url_accumulated(emparn):
    url = "http://meteorologia.emparn.rn.gov.br:8181/monitoramento/2020/acumulapr.htm"
    assert url in emparn.get_urls_accumulated()
