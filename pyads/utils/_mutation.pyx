"""
Collection of array mutation strategies for combinatorial 
optimisation applications.
"""

# cython: cdivision=True
# cython: boundscheck=False
# cython: wraparound=False

# Authors: Joseph Moorhouse <moorhouse@live.co.uk>
#
# License: BSD 3 clause

from cython cimport boundscheck, wraparound
cimport numpy as np
import numpy as np

cpdef np.ndarray[np.int32_t, ndim=2] _swap(
    np.ndarray[np.int32_t, ndim=2] arr, 
    np.ndarray[np.int32_t, ndim=2] indices):
    """2D vector row-rise swap mutation method"""
    
    cdef:
        Py_ssize_t idx, N = arr.shape[0]
        np.int32_t i, j
        
    for idx in range(N):
        i, j = indices[idx, 0], indices[idx, 1]
        arr[idx, i], arr[idx, j] = arr[idx, j], arr[idx,i]
    
    return arr

cpdef np.ndarray[np.int32_t, ndim=2] _reverse(
    np.ndarray[np.int32_t, ndim=2] arr, 
    np.ndarray[np.int32_t, ndim=2] indices):
    """2D vector row-rise reversion mutation method"""

    cdef:
        Py_ssize_t idx, N = arr.shape[0]
        np.int32_t i, j
    
    for idx in range(N):
        i, j = indices[idx, 0], indices[idx, 1]
        
        while i < j + 1:
            arr[idx,i], arr[idx,j] = arr[idx,j], arr[idx,i]
            i += 1
            j -= 1
    
    return arr

cpdef np.ndarray[np.int32_t, ndim=2] _insert(
    np.ndarray[np.int32_t, ndim=2] arr, 
    np.ndarray[np.int32_t, ndim=2] indices,
    int step = 1):
    """2D vector row-rise insertion mutation method"""
    
    cdef:
        Py_ssize_t i, j, N = arr.shape[0]
        np.int32_t start, stop, n, shift
            
    for i in range(N):
        start, stop = indices[i, 0], indices[i, 1] + 1
        n = stop - start
        shift= step % n
        
        while n > 0 and shift % n != 0:
            for j in range(shift):
                arr[i, start + j] =  arr[i, stop - shift + j] 
                arr[i, stop - shift + j] = arr[i, start + j]

            n, start = n - shift, start + shift
            shift = shift % n
            
    return arr