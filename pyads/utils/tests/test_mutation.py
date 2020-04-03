from .._mutation import (
    array_indices_swap2d,
    array_indices_reverse2d,
    array_indices_insert2d
)

import pytest
import numpy as np


# =============================================================================
# Fixtures
# =============================================================================

@pytest.fixture
def arr_testcase_one():
    arange = np.arange(10, dtype='int64')
    return np.repeat(arange[np.newaxis], 5, axis=0)

# =============================================================================
# Test arrays/expected 
# =============================================================================

testcase_one_indices = np.array(
    [[0,9], [3,5], [0,4], [8,9], [6,8]], 
    dtype='int64'
)

swap_one_expected = np.array([
    [9,1,2,3,4,5,6,7,8,0],
    [0,1,2,5,4,3,6,7,8,9],
    [4,1,2,3,0,5,6,7,8,9],
    [0,1,2,3,4,5,6,7,9,8],
    [0,1,2,3,4,5,8,7,6,9]
])

reverse_one_expected = np.array([
    [9,8,7,6,5,4,3,2,1,0],
    [0,1,2,5,4,3,6,7,8,9],
    [4,3,2,1,0,5,6,7,8,9],
    [0,1,2,3,4,5,6,7,9,8],
    [0,1,2,3,4,5,8,7,6,9]
])

insert_one_expected = np.array([
    [9,0,1,2,3,4,5,6,7,8],
    [0,1,2,5,3,4,6,7,8,9],
    [4,0,1,2,3,5,6,7,8,9],
    [0,1,2,3,4,5,6,7,9,8],
    [0,1,2,3,4,5,8,6,7,9]
])
    


# =============================================================================
# Tests
# =============================================================================

@pytest.mark.parametrize(
    'test_input, expected', 
    [(testcase_one_indices, swap_one_expected)])
def test_swap(arr_testcase_one, test_input, expected):
    arr = array_indices_swap2d(arr_testcase_one, testcase_one_indices)
    assert (arr == swap_one_expected).all()

@pytest.mark.parametrize(
    'test_input, expected', 
    [(testcase_one_indices, reverse_one_expected)])
def test_reverse(arr_testcase_one, test_input, expected):
    arr = array_indices_reverse2d(arr_testcase_one, testcase_one_indices)
    assert (arr == reverse_one_expected).all()

@pytest.mark.parametrize(
    'test_input, expected', 
    [(testcase_one_indices, insert_one_expected)])
def test_insert(arr_testcase_one, test_input, expected):
    arr = array_indices_insert2d(arr_testcase_one, testcase_one_indices)
    assert (arr == insert_one_expected).all()