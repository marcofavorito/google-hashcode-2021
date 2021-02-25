# -*- coding: utf-8 -*-

"""All lights, 1 second."""

from typing import List
from hashcode.common.model import Schedule
from hashcode.common.base import Input, Output


def main(i: Input) -> Output:
    """All lights, 1 second."""
    schedules: List[Schedule] = []

    used_streets = {}
    for path in i.paths:
        for street in path.streets:
            if street.name not in used_streets:
                used_streets[street.name] = 0
            used_streets[street.name] += 1

    for intersection_id, intersection in i.intersections.items():
        green_lights = {}
        intersection_traffic = 0
        min_traffic = 1_000_000
        for street in intersection.in_streets:
            if street.name in used_streets:
                traffic = used_streets[street.name]
                min_traffic = min(min_traffic, traffic)
                intersection_traffic += traffic
        
        if intersection_traffic == 0:
            continue

        alpha = min_traffic / intersection_traffic
        for street in intersection.in_streets:
            if street.name in used_streets and used_streets[street.name] > 0:
                green_lights[street] = max(1, int(used_streets[street.name] * alpha))

        if green_lights:
            schedule = Schedule(intersection_id=intersection_id, green_light_streets=green_lights)
            schedules.append(schedule)
            
    return Output(schedule=schedules)