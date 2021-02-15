from asyncio import gather, run
from httpx import AsyncClient
from datetime import date
from lxml import html


base_url = "http://meteorologia.emparn.rn.gov.br:8181/monitoramento/{year}/graficos/d8101.html"


class Emparn:
    def __init__(self, city_code="d8101"):
        self.city_code = city_code
        self.current_year = date.today().year
        self.dataset = None

    async def download(self, year):
        async with AsyncClient() as client:
            response = await client.get(
                base_url.format(year=year), timeout=None
            )
            return response

    async def get_dataset(self, start):
        return await gather(
            *[
                self.download(year)
                for year in range(start, self.current_year + 1)
            ]
        )

    def data_processing(self, start_year=1992):

        data = run(self.get_dataset(start=start_year))
        count_year = 0
        dataset_months = []
        dataset_year = []
        for year in range(start_year, self.current_year + 1):
            if year % 4 == 0:
                months = [93, 87, 93, 90, 93, 90, 93, 93, 90, 93, 90, 93]
            else:
                months = [93, 84, 93, 90, 93, 90, 93, 93, 90, 93, 90, 93]
            content = html.fromstring(data[count_year].content)
            scraping = content.xpath("//td[text()>0]/../td/text()")
            month_counter = 0
            accumulated_month = 0
            year_to_date = []
            for m in range(12):
                count = 0
                for i in range(month_counter, months[m] + month_counter):
                    count += 1
                    if count != 3:
                        if count == 2:
                            try:
                                if float(scraping[i]) < 0:
                                    scraping[i] = 0
                                accumulated_month += float(scraping[i])
                            except IndexError:
                                break
                    else:
                        count = 0
                month_counter += months[m]
                dataset_months.append(round(accumulated_month, 3))
                year_to_date.append(round(accumulated_month, 3))
                accumulated_month = 0
            dataset_year.append(round(sum(year_to_date), 3))
            del year_to_date[:]
            count_year += 1
        return dataset_year, dataset_months

    def __repr__(self):
        return "Class Emparn"
