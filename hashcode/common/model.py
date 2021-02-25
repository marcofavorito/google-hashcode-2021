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
    street: Tuple[Street]


@dataclass(frozen=True, repr=True, eq=True)
class Schedule:
    intersection_id: int
    green_light_streets: Dict[Street, int]


@dataclass(repr=True, eq=True, unsafe_hash=True)
class Intersection:
    id: int
    in_streets: List[Street]
    out_streets: List[Street]
