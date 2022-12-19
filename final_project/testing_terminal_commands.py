""" Testing functions of terminal_commands.py"""
import terminal_commands as tc
import pizzas
import re


def test_deliver_of_tc():
    """Test 1"""
    result = tc.deliver(pizzas.Margherita('L'))
    assert re.sub(r'[0-9]', '', result) == 'Margherita 🚴 Deliver for  min!'


def test_pickup_of_tc():
    """Test 2"""
    result = tc.pickup(pizzas.Hawaiian('L'))
    assert re.sub(r'[0-9]', '', result) == 'Hawaiian 🚴 Pick up for  min!'


def test_preparing_of_tc():
    """Test 3"""
    result = tc.preparing(pizzas.Pepperoni('L'))
    assert re.sub(r'[0-9]', '', result) == 'Pepperoni 🥘 Prepare for  min!'
