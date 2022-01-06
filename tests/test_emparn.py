from datetime import datetime

from ifrn_estatistica.emparn import (accumulated_annual_rainfall,
                                     get_city_stations)


def test_emparn():
    city_stations = get_city_stations()
    response = accumulated_annual_rainfall(
        places=[city_stations["Natal"][1]],
        start_day=datetime(1992, 1, 1).isoformat() + "-03:00",
        final_day=datetime(2022, 1, 1).isoformat() + "-03:00",
    )
    assert response is not None
