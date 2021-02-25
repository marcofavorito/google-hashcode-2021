# -*- coding: utf-8 -*-
"""
Main functions and classes to handle a problem instance.

This module contains:

- Input class: to handle the input of a problem instance.
- Output class: to handle the output of the algorithm given an input.
- score function: takes as parameters an Input and an Output, and gives the score.
- (read|write)_(input|output): to read/write from/to file an Input/Output object.

The definitions of classes and function should be considered
stubs to be implemented for the actual problem.
"""
import sys
from dataclasses import dataclass
from typing import TextIO, Set, List, Tuple, Dict

from hashcode.common.model import Intersection, Street, CarPath, Schedule


@dataclass
class Input:
    """This data class manages the input of the problem."""

    duration_seconds: int
    nb_intersections: int
    nb_cars: int
    bonus_points: int
    streets: Set[Street]
    paths: Set[CarPath]
    intersections: Dict[int, Intersection]

    def __post_init__(self):
        """Post-initialization."""


@dataclass(frozen=True)
class Output:
    """This data class manages the output of the problem."""

    schedule: Tuple[Schedule] = tuple()

    @property
    def nb_intersections(self):
        return len(self.schedule)

    def __post_init__(self):
        """Post-initialization."""


def score(i: Input, o: Output) -> int:
    """
    Score the solution.

    :param i: the Input object.
    :param o: the Output object.
    :return: the score.
    """
    raise NotImplementedError


def read_input(input_stream: TextIO = sys.stdin) -> Input:
    """
    Parse an Input object from a text stream.

    :param input_stream: the input text stream.
    :return: an Input object
    """
    lines = [l.strip() for l in input_stream.readlines()]
    D, I, S, V, F = list(map(int, lines[0].split()))
    offset = 1
    streets: List[Street] = []
    for street_line in lines[offset: offset + S]:
        b, e, street_name, l = street_line.split()
        beginning = int(b)
        end = int(e)
        length = int(l)
        street = Street(street_name, beginning, end, length)
        streets.append(street)

    offset += S
    paths = []
    for path in lines[offset: offset + V]:
        tokens = path.split()
        street_names = tokens[1:]
        paths.append(CarPath(street_names))

    intersections = {}
    for street in streets:
        if street.beginning not in intersections:
            intersections[street.beginning] = Intersection(id=street.beginning, in_streets=[], out_streets=[])
        if street.end not in intersections:
            intersections[street.end] = Intersection(id=street.end, in_streets=[], out_streets=[])
        start_intersection = intersections[street.beginning]
        start_intersection.out_streets.append(street.name)
        end_intersection = intersections[street.end]
        end_intersection.in_streets.append(street.name)
            
    return Input(duration_seconds=D, nb_intersections=I, nb_cars=V, bonus_points=F, streets=streets, paths=paths, intersections=intersections)


def write_input(obj: Input, output_stream: TextIO = sys.stdout) -> None:
    """
    Dump an Input object to an output stream.

    :param obj: the object to dump.
    :param output_stream: the output stream.
    :return: None
    """
    raise NotImplementedError


def read_output(input_stream: TextIO = sys.stdin) -> Output:
    """
    Parse a text stream to produce an Output object.

    :param input_stream: the input text stream.
    :return: an Output object.
    """
    raise NotImplementedError


def write_output(obj: Output, output_stream: TextIO = sys.stdout) -> None:
    """
    Dump an Output object to an output stream.

    :param obj: the Output object.
    :param output_stream: the output text stream.
    :return: None
    """
    lines = []
    lines.append(str(obj.nb_intersections))
    for schedule in obj.schedule:
        lines.append(str(schedule.intersection_id))

        nb_incoming_streets = len(schedule.green_light_streets)
        lines.append(str(nb_incoming_streets))

        for street, seconds in schedule.green_light_streets.items():
            lines.append(f"{street.name} {seconds}")

    output_stream.writelines(lines)