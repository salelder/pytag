from .core import Tag
from . import tags

__version__ = "0.1.0"

# Get all tag functions from the tags module
import inspect
import sys

__all__ = ['Tag', 'Tags'] + [
    name for name, obj in inspect.getmembers(sys.modules[__name__])
    if inspect.isfunction(obj) and obj.__module__ == __name__
] 