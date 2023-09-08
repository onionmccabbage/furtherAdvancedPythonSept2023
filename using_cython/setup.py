from setuptools import setup
# may need to pip install cython
from Cython.Build import cythonize

# we really ought to validate our system, maybe read some sys.argv
setup(
    ext_modules=cythonize('sample.pyx')
)