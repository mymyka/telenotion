from abc import ABC, abstractmethod

import requests
from bs4 import BeautifulSoup


class Parser(ABC):
    def __init__(self, src: str):
        self._src: str = src

    @property
    @abstractmethod
    def cover(self) -> str:
        pass

    @property
    @abstractmethod
    def favicon(self) -> str:
        pass

    @property
    @abstractmethod
    def title(self) -> str:
        pass


class WebpageParser(Parser):
    __headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) '
                      'Gecko/20100101 Firefox/24.0'
    }

    def __init__(self, src: str):
        super().__init__(src)
        self.__webpage: BeautifulSoup = None

    def __enter__(self):
        self.load()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @property
    def cover(self) -> str:
        return 'https://media.istockphoto.com/id/1162219821/' \
               'vector/red-bookmark-icon-vector-flat-design.' \
               'jpg?s=612x612&w=0&k=20&c=CfguRebNu56EYm4SvSl' \
               '6QposTtVu2n73jw9H3eryCYU='

    @property
    def favicon(self) -> str:
        return self.__webpage.find('link', rel='icon')['href']

    @property
    def title(self) -> str:
        return self.__webpage.find('title').text

    def load(self):
        response = requests.get(url=self._src,
                                headers=self.__headers)
        self.__webpage = BeautifulSoup(response.text, 'html.parser')
