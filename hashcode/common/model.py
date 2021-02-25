# -*- coding: utf-8 -*-

"""Common classes to represent the problem."""
from dataclasses import dataclass
from typing import List


@dataclass
class Street:
    name: str
    beginning: int
    end: int
    length: int


@dataclass
class CarPath:
    names: List[str]
