""" Testing functions of pizzas.py"""
import pizzas


def test_eq_of_pizzas():
    """Test1"""
    assert (pizzas.Hawaiian('L') == pizzas.Pepperoni('XL')) is False
    assert (pizzas.Margherita('L') == pizzas.Margherita('L')) is True
    assert (pizzas.Pepperoni('L') == pizzas.Pepperoni('XL')) is False


def test_dict_of_pizzas():
    """Test 2"""
    assert pizzas.Margherita('L').dict() == {'name': 'Margherita 🧀',
                                             'recipe': ['tomato sauce',
                                                        'mozzarella',
                                                        'tomatoes']}
