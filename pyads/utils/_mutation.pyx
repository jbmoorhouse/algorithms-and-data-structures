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
from cython.parallel cimport prange
from numpy cimport ndarray as ar
cimport numpy as np

ctypedef np.int64_t DTYPE

cpdef ar[DTYPE, ndim=2] array_indices_swap2d(
    ar[DTYPE, ndim=2] arr, 
    ar[DTYPE, ndim=2] indices):
    """2D vector row-rise swap mutation method"""
    
    cdef:
        Py_ssize_t idx, N = arr.shape[0]
        DTYPE i, j
        
    for idx in range(N):
        i, j = indices[idx, 0], indices[idx, 1]
        arr[idx, i], arr[idx, j] = arr[idx, j], arr[idx,i]
    
    return arr
    

cpdef ar[DTYPE, ndim=2] array_indices_reverse2d(
    ar[DTYPE, ndim=2] arr, 
    ar[DTYPE, ndim=2] indices):
    """2D vector row-rise reversion mutation method"""

    cdef:
        Py_ssize_t idx, N = arr.shape[0]
        DTYPE i, j
    
    for idx in range(N):
        i, j = indices[idx, 0], indices[idx, 1]
        
        while i < j + 1:
            arr[idx,i], arr[idx,j] = arr[idx,j], arr[idx,i]
            i += 1
            j -= 1
    
    return arr

cpdef ar[DTYPE, ndim=2] array_indices_insert2d(
    ar[DTYPE, ndim=2] arr, 
    ar[DTYPE, ndim=2] indices,
    int step = 1):
    """2D vector row-rise insertion mutation method using cylic array
    rotation. See https://www.geeksforgeeks.org/array-rotation/"""
    
    cdef:
        Py_ssize_t i, j, N = arr.shape[0]
        DTYPE start, stop, n, shift
            
    for i in range(N):
        start, stop = indices[i, 0], indices[i, 1] + 1
        n = stop - start
        shift = step % n
        
        while n > 0 and shift % n != 0:
            for j in range(shift):
                temp = arr[i, start + j]
                arr[i, start + j] = arr[i, stop - shift + j]
                arr[i, stop - shift + j] = temp
                
            n, start = n - shift, start + shift
            shift = shift % n
            
    return arr

cpdef ar[DTYPE, ndim=2] array_indices_insert2d(
    ar[DTYPE, ndim=2] arr, 
    ar[DTYPE, ndim=2] indices,
    DTYPE step = 1):
    """2D vector row-rise insertion mutation method using cylic array
    rotation. See https://www.geeksforgeeks.org/array-rotation/"""
    
    cdef:
        DTYPE i, j, N = arr.shape[0]
        DTYPE start, stop, n, shift, temp
        
    with nogil:        
        for i in prange(N):
            start, stop = indices[i, 0], indices[i, 1] + 1
            n = stop - start
            shift = step % n
            
            while n > 0 and shift % n != 0:
                for j in range(shift):
                    temp = arr[i, start + j]
                    arr[i, start + j] = arr[i, stop - shift + j]
                    arr[i, stop - shift + j] = temp
                    
                n, start = n - shift, start + shift
                shift = shift % n
            
    return arr