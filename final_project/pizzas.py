""""Classes for recipes of pizzas"""


class Pizza:
    """Main class for all pizzas"""
    def __eq__(self, other: 'Pizza'):
        if set(self.recipe) == set(other.recipe) \
           and self.size == other.size:
            return True
        return False

    @classmethod
    def dict(cls):
        """Just return recipe as dict"""
        return {'name': cls.__name__ + ' ' + cls.emoji,
                'recipe': cls.recipe}


class Margherita(Pizza):
    """Class for pizza Margherita"""
    recipe = ['tomato sauce', 'mozzarella', 'tomatoes']
    emoji = '🧀'

    def __init__(self, size: str):
        self.size = size
        self.time = 30 if size == 'L' else 45


class Pepperoni(Pizza):
    """Class for pizza Pepperoni"""
    recipe = ['tomato sauce', 'mozzarella', 'pepperoni']
    emoji = '🌶'

    def __init__(self, size: str):
        self.size = size
        self.time = 25 if size == 'L' else 30


class Hawaiian(Pizza):
    """Class for pizza Hawaiian"""
    recipe = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']
    emoji = '🍍'

    def __init__(self, size: str):
        self.size = size
        self.time = 50 if size == 'L' else 60


MENU_DICT = {'margherita': Margherita,
             'pepperoni': Pepperoni,
             'hawaiian': Hawaiian}
