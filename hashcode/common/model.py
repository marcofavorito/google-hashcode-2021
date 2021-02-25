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
    streets: Tuple[Street]

    @property
    def nb_streets(self) -> int:
        return len(self.streets)

    @property
    def length(self) -> int:
        return sum([s.length for s in self.streets])

    def __len__(self) -> int:
        return self.nb_streets


@dataclass(frozen=True, repr=True, eq=True)
class Schedule:
    intersection_id: int
    green_light_streets: Dict[Street, int]


@dataclass(repr=True, eq=True, unsafe_hash=True)
class Intersection:
    id: int
    in_streets: List[Street]
    out_streets: List[Street]
