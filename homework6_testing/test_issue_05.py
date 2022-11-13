"""Testing what_is_year_now function"""
import pytest
from unittest.mock import patch
from what_is_year_now import what_is_year_now


def test_year1():
    """Test 1"""
    with patch('json.load') as mocked_get_cases:
        mocked_get_cases.return_value = {'currentDateTime': '2022-11-13'}
        assert what_is_year_now() == 2022


def test_year2():
    """Test 2"""
    with patch('json.load') as mocked_get_cases:
        mocked_get_cases.return_value = {'currentDateTime': '13.11.2022'}
        assert what_is_year_now() == 2022


def test_year3():
    """Test 3"""
    with patch('json.load') as mocked_get_cases:
        mocked_get_cases.return_value = {'currentDateTime': '13-11-2022'}
        with pytest.raises(ValueError):
            what_is_year_now()


def test_year4():
    """Test 4"""
    with patch('json.load') as mocked_get_cases:
        mocked_get_cases.return_value = {'DateTime': '13-11-2022'}
        with pytest.raises(KeyError):
            what_is_year_now()
