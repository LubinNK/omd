"""Testing encode function in morse.py"""
import doctest
from morse import encode


def test_encode(message: str):
    """
    Testing encode function

    >>> test_encode('SOS')
    '... --- ...'
    >>> test_encode('+') # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    KeyError: '+'
    """
    return encode(message)


if __name__ == '__main__':
    doctest.testmod()
