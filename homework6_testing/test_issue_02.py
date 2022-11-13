"""Testing decode function in morse.py"""
from morse import decode
import pytest


@pytest.mark.parametrize(
    'test_input,expected',
    [('..--- ----- .---- ----.', '2019'),
     ('... --- ...', 'SOS'),
     ('-.- --- .-.. -.-- .-', 'KOLYA'),
     ('-.- --- .-.. -.-- .-', 'KOL')]
)
def test_decode(test_input, expected):
    """Testing function for decode"""
    assert decode(test_input) == expected
