"""
Module: test_mathematics.py
Description: This module contains unit tests for the functions in the mathematics module.
"""

from typing import List, Union

import pytest

from src.mathematics import sum_array


@pytest.mark.parametrize(
    "input_array, expected_output",
    [
        ([1, 2, 3], 6),
        ([1.5, 2.5, 3.5], 7.5),
        ([0, 0, 0], 0),
        ([], 0),
        ([1, -1, 2], 2),
    ],
)
def test_sum_array(
    input_array: List[Union[int, float]], expected_output: Union[int, float]
) -> None:
    """
    Test the sum_array function with various inputs.

    Parameters
    ----------
    input_array : List[int, float]
        Input array of integers or floats.
    expected_output : int
        Expected sum of the elements in the array.
    """
    result = sum_array(input_array)
    assert result == expected_output
