""" Working with classes and JSON objects """
import json
from keyword import iskeyword


class JSONReader:
    """JSON to Python objects"""
    def __init__(self, dict_json: dict):
        for attr, val_attr in dict_json.items():
            if isinstance(val_attr, dict):
                setattr(self, self.is_key(attr), JSONReader(val_attr))
            else:
                setattr(self, self.is_key(attr), val_attr)

    @staticmethod
    def is_key(word: str):
        """Check if word is keyword, and change it if yes"""
        if iskeyword(word) or word == 'price':
            word = ''.join(list(word)+['_'])
        return word


class ColorizeMixin:
    """ Print with color """
    def __repr__(self):
        return f'\033[{self.repr_color_code}m {self.title} | {self.price} $'


class BaseAdvert(JSONReader):
    """For adverb"""

    def __init__(self, adv: dict):
        self._norm_title = True
        self._norm_price = True
        if 'title' not in adv:
            self._norm_title = False
        if 'price' not in adv:
            self.price_ = 0
        elif adv['price'] < 0:
            self._norm_price = False
        if not self._norm_title:
            raise ValueError('Title is the necessary attribute!')
        if not self._norm_price:
            raise ValueError('Price must be >= 0.')
        super().__init__(adv)

    @property
    def price(self):
        """Price property"""
        return self.price_

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price must be >= 0")
        self.price_ = value

    def __repr__(self):
        return f'{self.title} | {self.price} $'


class Advert(ColorizeMixin, BaseAdvert):
    """Main Class Advert"""
    repr_color_code = 32


def main():
    """Main Launch"""
    lesson_str = """{
        "title": "python",
        "class": "lesson",
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
        }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.location.address)
    print(lesson_ad.price)
    print(lesson_ad.class_)
    print(lesson_ad)


if __name__ == '__main__':
    main()
