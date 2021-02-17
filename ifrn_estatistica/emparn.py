from asyncio import gather, run
from typing import List, Tuple
from copy import deepcopy
from urllib.parse import urljoin
from datetime import date
from os.path import isfile
from pandas import DataFrame
from httpx import AsyncClient
from lxml import html


class Emparn:
    def __init__(self, cities: List, starting_year=1992, keep=False):
        self.cities = cities
        self.keep = keep
        self.current_year = date.today().year
        self.starting_year = starting_year

    async def download(self, url):
        async with AsyncClient() as client:
            response = await client.get(url, timeout=None)
            return response

    async def get_dataset(self, urls):
        return await gather(*[self.download(url) for url in urls])

    def get_urls_accumulated(self) -> List:

        usrbase = "http://meteorologia.emparn.rn.gov.br:8181/monitoramento/{year}/acumulapr.htm"

        return [
            usrbase.replace("{year}", str(year))
            for year in range(self.starting_year, self.current_year)
        ]

    def get_city_data(self) -> Tuple:
        """Método para scriping de dados das cidades.
           Returns:
                Tuple - tupla com dois dicts um com links
                para download de dados brutos e outro
                com o acumulado do ano.
        """

        urls = self.get_urls_accumulated()
        data = run(self.get_dataset(urls))
        city_dataset = {}
        dataset = []
        for i in range(len(self.cities)):
            for j in range(len(data)):
                content = html.fromstring(data[j].content)
                scraping_url = content.xpath(
                    f"//*[contains(text(),'{self.cities[i].upper()}')]/../td/a/@href"
                )[3]
                scraping_accumulated = content.xpath(
                    f"//*[contains(text(),'{self.cities[i].upper()}')]/../td/text()"
                )[1]
                dataset.append((scraping_url, scraping_accumulated))
            city_dataset[self.cities[i].upper()] = deepcopy(dataset)
            del dataset[:]

        links = {}
        links_tmp = []
        accumulated = {}
        accumulated_tmp = {}
        starting_year = self.starting_year
        for k in city_dataset.keys():
            for i in range((self.current_year - self.starting_year)):
                url_base = f"http://meteorologia.emparn.rn.gov.br:8181/monitoramento/{starting_year}/"
                links_tmp.append(urljoin(url_base, city_dataset[k][i][0]))
                accumulated_tmp[starting_year] = city_dataset[k][i][1]
                starting_year += 1
            starting_year = self.starting_year
            links[k] = deepcopy(links_tmp)
            del links_tmp[:]
            accumulated[k] = deepcopy(accumulated_tmp)

        if self.keep:
            if not isfile(f"{date.today()}_links_raw_data.csv"):
                df = DataFrame(links)
                df.to_csv(f"{date.today()}_links_raw_data.csv")

            if not isfile(f"{date.today()}_accumulated.csv"):
                df = DataFrame(accumulated)
                df.to_csv(f"{date.today()}_accumulated.csv")

        return links, accumulated

    def raw_city_data(self):

        links, _ = self.get_city_data()
        data = run(
            self.get_dataset(
                [
                    v[i]
                    for v in links.values()
                    for i in range((self.current_year - self.starting_year))
                ]
            )
        )
        count_data = 0
        dataset_city = {}
        dataset_years = {}
        dataset_months = []
        for city in self.cities:
            for year in range(self.starting_year, self.current_year):
                if year % 4 == 0:
                    months = [93, 87, 93, 90, 93, 90, 93, 93, 90, 93, 90, 93]
                else:
                    months = [93, 84, 93, 90, 93, 90, 93, 93, 90, 93, 90, 93]
                content = html.fromstring(data[count_data].content)
                scraping = content.xpath("//td[text()>0]/../td/text()")
                month_counter = 0
                accumulated_month = 0
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
                    accumulated_month = 0
                dataset_years[year] = deepcopy(dataset_months)
                del dataset_months[:]
                count_data += 1
            dataset_city[city] = deepcopy(dataset_years)
        if self.keep:
            for k in dataset_city.keys():
                df = DataFrame(dataset_city[k])
                if not isfile(f"{date.today()}_raw_data_{k}.csv"):
                    df.to_csv(f"{date.today()}_raw_data_{k}.csv")
        return dataset_city

    def __repr__(self):
        return "Class Emparn"
