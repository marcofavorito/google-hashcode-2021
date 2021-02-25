# -*- coding: utf-8 -*-

"""A minimum working example."""
from collections import defaultdict
from typing import List, Dict

from hashcode.common.base import Input, Output
from hashcode.common.model import Schedule, Street, CarPath, Intersection

# schedules: List[Schedule] = []
# paths_sorted_by_length = sorted(i.paths, key=lambda p: len(p))
# street_to_cost: Dict[Street, int] = {s: s.length for s in i.streets}
# def cost_of_path(p: CarPath) -> int:
#     return sum([s.length for s in p.streets])
# paths_sorted_by_cost = sorted(i.paths, key=cost_of_path)


def main(i: Input) -> Output:
    """Minimum working algorithm."""
    schedules: List[Schedule] = []

    counts_in_streets_by_intersection_id: Dict[int, Dict[Street, int]] = defaultdict(lambda: defaultdict(lambda: 0))
    counts_by_intersection: Dict[int, int] = defaultdict(lambda: 0)

    for path in i.paths:
        for street in path.streets:
            counts_in_streets_by_intersection_id[street.end][street] += 1
            counts_by_intersection[street.end] += 1

    for intersection_id, total_counts in counts_by_intersection.items():
        count_by_streets: Dict[Street, int] = counts_in_streets_by_intersection_id[intersection_id]

        total_period_duration = len(count_by_streets) * 2
        compute_time = lambda count: int(count * total_period_duration // total_counts)

        green_lights: Dict[Street, int] = {s: max(1, compute_time(c)) for s, c in count_by_streets.items()}

        # print("-"*100)
        # print(total_period_duration)
        # print(sorted(green_lights.values()))

        schedule = Schedule(intersection_id=intersection_id, green_light_streets=green_lights)
        schedules.append(schedule)

    return Output(tuple(schedules))