# -*- coding: utf-8 -*-

"""Common classes to represent the problem."""
from dataclasses import dataclass
from typing import List, Set, Tuple, FrozenSet, Dict


@dataclass(frozen=True, repr=True, eq=True, unsafe_hash=True)
class Street:
    name: str
    beginning: int
    end: int
    length: int


@dataclass(frozen=True, repr=True, eq=True, unsafe_hash=True)
class CarPath:
    names: Tuple[str]


@dataclass(frozen=True, repr=True, eq=True)
class Schedule:
    intersection_id: int
    green_light_streets: Dict[Street, int]
