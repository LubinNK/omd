""" Testing functions of Project """
import re
import terminal_commands as tc
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


def test_deliver_of_tc():
    """Test 3"""
    result = tc.deliver(pizzas.Margherita('L'))
    assert re.sub(r'[0-9]', '', result) == 'Margherita 🚴 Deliver for  min!'


def test_pickup_of_tc():
    """Test 4"""
    result = tc.pickup(pizzas.Hawaiian('L'))
    assert re.sub(r'[0-9]', '', result) == 'Hawaiian 🚴 Pick up for  min!'


def test_preparing_of_tc():
    """Test 5"""
    result = tc.preparing(pizzas.Pepperoni('L'))
    assert re.sub(r'[0-9]', '', result) == 'Pepperoni 🥘 Prepare for  min!'
