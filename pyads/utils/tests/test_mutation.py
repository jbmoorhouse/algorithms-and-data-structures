#from .._mutation import array_indices_swap2d

import pytest
import numpy as np


# =============================================================================
# Fixtures
# =============================================================================

# @pytest.fixture
# def arr_testcase_one():
#     arange = np.arange(10, dtype='int64')
#     return np.repeat(arange[np.newaxis], 5, axis=0)

# # =============================================================================
# # Test/expected
# # =============================================================================

# test_one_input = np.array(
#     [[0, arr_testcase_one.shape[1] - 1], [3,5], [0,4], [8,9], [6,8]], 
#     dtype='int64'
# )

# test_one_expected = np.array([
#     [9,1,2,3,4,5,6,7,8,0],
#     [0,1,2,5,4,3,6,7,8,9],
#     [4,1,2,3,0,5,6,7,8,9],
#     [0,1,2,3,4,5,6,7,9,8],
#     [0,1,2,3,4,5,8,7,6,9]
# ])

# # =============================================================================
# # Test swap
# # =============================================================================

# @pytest.mark.parametrize(
#     'test_input, expected', 
#     [test_one_input, test_one_expected])
# def test_swap(arr_testcase_one):
#     arr = array_indices_swap2d(arr_testcase_one, test_one_input)
#     assert arr == test_one_expected