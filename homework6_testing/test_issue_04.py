"""Testing fit_transform with pytest"""
import pytest
from one_hot_encoding import fit_transform


@pytest.mark.parametrize(
    'test_input,expected',
    [
        (
            ['Moscow', 'New York', 'Moscow', 'London'],
            [
                ('Moscow', [0, 0, 1]),
                ('New York', [0, 1, 0]),
                ('Moscow', [0, 0, 1]),
                ('London', [1, 0, 0])
            ]
        ),
        (
            ['Tree', 'Sun'],
            [
                ('Tree', [0, 1]),
                ('Sun', [1, 0])
            ]
        )
    ]
)
def test_ft1(test_input, expected):
    """Test 1"""
    assert fit_transform(test_input) == expected


def test_ft2_empty():
    """Test 2"""
    assert fit_transform(['1', 2]) == []


def test_ft3():
    """Test 3"""
    tf_obj = fit_transform(['Tree', 'Sun'])
    assert tf_obj[0][1] != tf_obj[1][1]


def test_ft4():
    """Test 4"""
    with pytest.raises(TypeError):
        fit_transform([[0, 3], 'Sun'])
