from setuptools import setup
import numpy as np
from Cython.Build import cythonize

def compile_cython_files():
    setup(
        name = "_mutation",
        ext_modules = cythonize("_mutation.pyx"),
        include_dirs=[np.get_include()],
        extra_compile_args=['-fopenmp'],
        extra_link_args=['-fopenmp']
    )

if __name__ == "__main__":
    compile_cython_files()