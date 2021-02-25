# -*- coding: utf-8 -*-

"""All lights, 1 second."""

from typing import List
from hashcode.common.model import Schedule
from hashcode.common.base import Input, Output


def main(i: Input) -> Output:
    """All lights, 1 second."""
    schedules: List[Schedule] = []
    for intersection_id, intersection in i.intersections.items():
        green_lights = {}
        for street in intersection.in_streets:
            green_lights[street] = 1

        schedule = Schedule(intersection_id=intersection_id, green_light_streets=green_lights)
        schedules.append(schedule)
            
    return Output(schedule=schedules)