import sys
from datetime.date import today
from lxml import html
from requests import get


class Emparn:
    def __init__(self, city_code):
        self.city_code = city_code
        self.current_year = today().year
        self.dataset = None

    def get_dataset(self):
        ...
        """        for iano in range(1992, self.current_year):
                # TRATAMENTO DE ANO BISSEXTO --------------------------------------
                if iano % 4 == 0:
                    qdmes = [93, 87, 93, 90, 93, 90, 93, 93, 90, 93, 90, 93]
                else:
                    qdmes = [93, 84, 93, 90, 93, 90, 93, 93, 90, 93, 90, 93]
                # -----------------------------------------------------------------
                url = f"http://meteorologia.emparn.rn.gov.br:8181/monitoramento/{iano}/graficos/d8101.html"
                try:
                    pagina = get(url)
                    if pagina.status_code != 200:
                        print(f"pagina não  encontrada erro{pagina.status_code}")
                        sys.exit()
                except (ConnectionError, OSError):
                    print("Ocorreu um erro, site fora do ar")
                    sys.exit()
                conteudo = html.fromstring(pagina.content)
                busca = conteudo.xpath("//td[text()>0]/../td/text()")
                contmes = 0
                acumuladomes = 0
                for imes in range(len(qdmes)):
                    cont = 0
                    for i in range(contmes, qdmes[imes] + contmes):
                        cont += 1
                        if cont != 3:
                            if cont == 2:
                                try:
                                    if float(busca[i]) < 0:
                                        busca[i] = 0
                                    acumuladomes += float(busca[i])
                                except IndexError:
                                    break
                        else:
                            cont = 0
                    contmes += qdmes[imes]
                    df.append(round(acumuladomes, 3))
                    acumuladomes = 0
            return df"""

    def __repr__(self):
        return "Class Emparn"
