# operations/__init__.py

from .Project import Project
from .Select import Select
from .Join import Join
from .CartesianProduct import CartesianProduct

# Expose the imported classes to make importing them easier
__all__ = ["Project", "Select", "Join", "CartesianProduct"]