""" Working with classes and JSON objects """
import json


class JSONReader:
    """JSON to Python objects"""
    def __init__(self, dict_json: dict):
        for attr, val_attr in dict_json.items():
            if isinstance(val_attr, dict):
                setattr(self, attr, JSONReader(val_attr))
            else:
                setattr(self, attr, val_attr)


class ColorizeMixin:
    """ Print with color """
    def __repr__(self):
        return f'\033[{self.repr_color_code}m {self.title} | {self.price} $'


class Advert(ColorizeMixin, JSONReader):
    """For adverb"""
    repr_color_code = 32

    def __init__(self, adv: dict):
        if 'price' in adv and adv['price'] >= 0:
            super().__init__(adv)
        elif 'price' in adv:
            raise ValueError('price must be >= 0')
        else:
            self.price = 0
            super().__init__(adv)

    def __repr__(self):
        return super().__repr__()


def main():
    """Main Launch"""
    lesson_str = """{
        "title": "python",
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
        }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.location.address)
    print(lesson_ad.price)
    print(lesson_ad)


if __name__ == '__main__':
    main()
