import time

import requests
from tqdm import tqdm

from parser.models import AuthorModel, CategoryModel, BookModel, PublisherModel
from bot.app.database import Insert


class Parser:
    """
    Summary
        The Parser class is responsible for parsing data from a website and inserting it into a database. It makes use
        of the requests library to send HTTP requests and the Insert class to insert data into the database.

    Main functionalities
        Sending HTTP requests to a website and retrieving JSON data.
        Parsing the JSON data and extracting relevant information.
        Inserting the extracted information into a database using the Insert class.

    Methods
        __init__(self, url: str, headers: dict, cookies: dict): Initializes the Parser object with the URL of the
            website, headers, and cookies.
        parse(self): Parses the data from the website by sending HTTP requests, extracting relevant information, and
            inserting it into the database.

    Fields
        url: str: The URL of the website to parse.
        headers: dict: The headers to be included in the HTTP requests.
        cookies: dict: The cookies to be included in the HTTP requests.
    """

    def __init__(self, url: str, headers: dict, cookies: dict):
        self.url = url
        self.headers = headers
        self.cookies = cookies

    def parse(self):
        """
        Summary
            The parse method in the Parser class is responsible for parsing data from a website and inserting it into a
            database. It sends HTTP requests to the website, retrieves JSON data, extracts relevant information, and
            inserts it into the database using the Insert class.

        Inputs
            url (str): The URL of the website to parse.
            headers (dict): The headers to be included in the HTTP requests.
            cookies (dict): The cookies to be included in the HTTP requests.

        Flow
            The method initializes the Parser object with the provided URL, headers, and cookies.
            It iterates over a range of numbers from 1 to 447.
            For each number, it sends an HTTP request to the website with specific parameters.
            It retrieves the JSON data from the response.
            It creates an instance of the Insert class.
            It iterates over the data in the JSON response.
            It extracts relevant information such as authors, category, publisher, and book details.
            It inserts the extracted information into the database using the methods of the Insert class.

        Outputs
            The method does not return any output. It inserts the parsed data into the database.
        """
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
