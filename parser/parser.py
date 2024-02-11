import os
import time

import requests
from tqdm import tqdm

from models import AuthorModel, CategoryModel, BookModel, PublisherModel
from models_orm import Insert


class Parser:

    def __init__(self, url: str, headers: dict, cookies: dict):
        self.url = url
        self.headers = headers
        self.cookies = cookies

    def parse(self):
        for n in tqdm(range(1, 447)):
            time.sleep(2)
            params = {
                'filters[onlyNotOnSale]': '1',
                'forceFilters[categories]': '18030',
                'products[page]': n,
                'products[per-page]': '1000',
                'sortPreset': 'relevance',
                'include': 'productTexts,publisher,publisherBrand,publisherSeries,dates,literatureWorkCycles,rating',
            }

            res = requests.get(url=self.url, params=params, cookies=self.cookies, headers=self.headers).json()
            inserter = Insert()

            for i in range(1000):
                path = res['data'][i].get('attributes')
                authors = path.get('authors')

                author = {}
                if len(authors) != 0:
                    author_ = AuthorModel(id=authors[0].get('id', 0),
                                          firstname=authors[0].get('firstName', 'ND'),
                                          lastname=authors[0].get('lastName', 'ND')
                                          )
                    author['author'] = author_.id
                    inserter.insert_author(id=author_.id, firstname=author_.firstname, lastname=author_.lastname)

                category = path.get('category')
                cat = CategoryModel(id=category.get('id', 0), title=category.get('title', 'ND'))
                inserter.insert_category(id=cat.id, title=cat.title)

                publisher = path.get('publisher')
                pub_id = {}

                if publisher:
                    pub = PublisherModel(id=publisher.get('id', 0), title=publisher.get('title', 'ND'))
                    pub_id['pub'] = pub.id
                    inserter.insert_publisher(id=pub.id, title=pub.title)

                book = BookModel(id=path.get('id'), author=author.get('author', 0), title=path.get('title'),
                                 description=path.get('description'), category=cat.id, publisher=pub_id.get('pub', 0),
                                 rating=path.get('rating').get('count', .0), votes=path.get('rating').get('votes', 0))

                inserter.insert_book(id=book.id, author=book.author, title=book.title,
                                     description=book.description, category=book.category, publisher=book.publisher,
                                     rating=book.rating, votes=book.votes)
