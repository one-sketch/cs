"""
CSCI-141 Computer Science 1 Recitation
11-Linked Lists

FrozenNode is used for immutable lists, and MutableNode for mutable lists.
"""

from typing import Any, Union
from dataclasses import dataclass


@dataclass(frozen=True)
class FrozenNode:
    """
    An immutable link node containing a value and a link to the next node
    """
    value: Any
    next: Union[None, 'FrozenNode']


@dataclass(frozen=False)
class MutableNode:
    """
    A mutable link node containing a value and a link to the next node
    """
    value: Any
    next: Union[None, 'MutableNode']