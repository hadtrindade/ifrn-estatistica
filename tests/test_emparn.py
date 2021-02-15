"""import pytest
from unittest.mock import Mock
from ifrn_estatistica.emparn import Emparn


@pytest.fixture
def emparn(mocker):
    response_mock = Mock()
    response_mock.get_dataset.return_value = b'<html xmlns:mml="http://www.w3.org/1998/Math/MathML">\n<head>\n<title> R output </title>\n<link rel=stylesheet href="R2HTML.css" type=text/css>\n<object id="mathplayer" classid="clsid:32F66A20-7614-11D4-BD11-00104BD3F987"></object>\n<?import namespace="mml" implementation="#mathplayer"?>\n<script type="text/javascript" src="ASCIIMathML.js"></script>\n<link href="./runtime/styles/xp/grid.css" rel="stylesheet" type="text/css" ></link>\n<link href="gridR2HTML.css" rel="stylesheet" type="text/css" ></link>\n\n<script src="./runtime/lib/grid.js"></script>\n\n<script src="./gridR2HTML.js"></script>\n<script>\n   nequations=0;\n</script>\n</head>\n<body onload="translate()" bgcolor= #FFFFFF >\n<p class=\'character\'><meta http-equiv=\'content-type\' content=\'text/html; charset=ISO-8859-1\' /></p>\n\n<p class=\'character\'><input type=\'button\' value=\'Retornar para p\xe1gina anterior\' onclick=\'history.go(-1)\' ></p>\n\n<p class=\'character\'><b>Posto: NATAL(NATAL-UFRN) </b></p>\n\n<p class=\'character\'><table border=1 rules=all frame=box cellpadding=5 cellspacing=0> <tr></p>\n\n<p class=\'character\'><td> Data </td> <td align=\'right\'>Precipita\xe7\xe3o(mm)</td> </td></tr></p>\n\n<p class=\'character\'><td> 01/01/2000 </td>   <td align=\'right\'>5.2 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 02/01/2000 </td>   <td align=\'right\'>0 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 03/01/2000 </td>   <td align=\'right\'>4 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 04/01/2000 </td>   <td align=\'right\'>0.9 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 05/01/2000 </td>   <td align=\'right\'>6.2 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 06/01/2000 </td>   <td align=\'right\'>0.4 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 07/01/2000 </td>   <td align=\'right\'>0 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 08/01/2000 </td>   <td align=\'right\'>0 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 09/01/2000 </td>   <td align=\'right\'>4.4 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 10/01/2000 </td>   <td align=\'right\'>5.4 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 11/01/2000 </td>   <td align=\'right\'>0.3 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 12/01/2000 </td>   <td align=\'right\'>0 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 13/01/2000 </td>   <td align=\'right\'>0 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 14/01/2000 </td>   <td align=\'right\'>0 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 15/01/2000 </td>   <td align=\'right\'>0 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 16/01/2000 </td>   <td align=\'right\'>0 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 17/01/2000 </td>   <td align=\'right\'>10.8 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 18/01/2000 </td>   <td align=\'right\'>1.8 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 19/01/2000 </td>   <td align=\'right\'>0 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 20/01/2000 </td>   <td align=\'right\'>0 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 21/01/2000 </td>   <td align=\'right\'>0 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 22/01/2000 </td>   <td align=\'right\'>0 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 23/01/2000 </td>   <td align=\'right\'>0 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 24/01/2000 </td>   <td align=\'right\'>0 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 25/01/2000 </td>   <td align=\'right\'>0 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 26/01/2000 </td>   <td align=\'right\'>0 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 27/01/2000 </td>   <td align=\'right\'>0 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 28/01/2000 </td>   <td align=\'right\'>0 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 29/01/2000 </td>   <td align=\'right\'>0 </td> <td> * </td></tr></p>\n\n<p class=\'character\'><td> 30/01/2000 </td>   <td align=\'right\'>0 </td> <td> * </td></tr><p class=\'character\'><td> 31/12/2000 </td>   <td align=\'right\'>1.4 </td> <td> * </td></tr></p>\n\n<p class=\'character\'></table></p>\n\n<p class=\'character\'><table border=1 rules=none frame=void cellpadding=5 cellspacing=0> <tr></p>\n\n<p class=\'character\'><td>Legendas: </td> <td>*  Dados consistidos </td></tr></p>\n\n<p class=\'character\'><td>            </td> <td>** Dados n\xe3o consistidos </td></tr></p>\n\n<p class=\'character\'><td>            </td> <td>-1 Aus\xeancia de dados</td></tr></p>\n\n<p class=\'character\'></table></p>\n\n<hr size=1>\n<font size=-1>\n\t Generated on: <i>Wed Nov 23 10:41:59 2011</i> - <b>R2HTML</b> \n<hr size=1>\n\t</body>\n</html>']
    get_mock = mocker.patch("ifrn_estatistica.emparn.Emparn.get_dataset")
    get_mock.return_Value = response_mock

    e = Emparn()
    return e.data_processing(start_year=2020)


@pytest.mark.parametrize(
    "value",
    [2161.2, 16.4]
)
def test_get_dataset_years(emparn, value):
    assert value in emparn[0]


import pytest
from unittest.mock import Mock
from ifrn_estatistica.emparn import Emparn


@pytest.fixture(scope="module")
def emparn():
    e = Emparn()
    return e.data_processing(start_year=2020)


@pytest.mark.parametrize("value", [2161.2, 16.4])
def test_get_dataset_years(emparn, value):
    assert value in emparn[0]


@pytest.mark.parametrize(
    "value",
    [
        184.7,
        202.4,
        433.5,
        228.2,
        428.2,
        276.0,
        235.2,
        33.2,
        41.0,
        34.6,
        39.8,
        24.4,
        16.2,
        0.2,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ],
)
def test_get_dataset_months(emparn, value):
    assert value in emparn[1]
"""