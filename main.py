import os

from parser.parser import Parser
from config import url, headers, cookies


Parser(url=url, headers=headers, cookies=cookies).parse()
