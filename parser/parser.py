import os
import sqlite3 as sql


import requests




class Connector:

    def __init__(self, filename):
        self.filename = filename

    def connector(self):
        return sql.connect(os.path.join(self.filename, '.sqlite3'))


class CreateDB:

    def __init__(self, filename):
        self.filename = filename
        self.connector = Connector.connector(self.filename)

    def create_tables(self):
        pass


class Parser:

    def __init__(self, url: str, headers: dict, cookies: dict):
        self.url = url
        self.headers = headers
        self.cookies = cookies

    def parse(self):
        for n in range(1, 447):
            params = {
                'filters[onlyNotOnSale]': '1',
                'forceFilters[categories]': '18030',
                'products[page]': n,
                'products[per-page]': '1000',
                'sortPreset': 'relevance',
                'include': 'productTexts,publisher,publisherBrand,publisherSeries,dates,literatureWorkCycles,rating',
            }

            res = requests.get(url=self.url, params=params, cookies=self.cookies, headers=self.headers).json()

