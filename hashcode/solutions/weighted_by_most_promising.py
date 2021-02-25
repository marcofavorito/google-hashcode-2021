# -*- coding: utf-8 -*-

"""A minimum working example."""
from collections import defaultdict
from functools import partial
from typing import List, Dict, Tuple

from hashcode.common.base import Input, Output
from hashcode.common.model import Schedule, Street, CarPath, Intersection


def optimal_score_(p: CarPath, duration: int = -1, bonus: int = -1) -> int:
    T = sum([s.length for s in p.streets])
    return bonus + (duration - T)


def main(i: Input) -> Output:
    """Minimum working algorithm."""
    schedules: List[Schedule] = []

    optimal_score = partial(optimal_score_, duration=i.duration_seconds, bonus=i.bonus_points)
    path_and_scores: List[Tuple[CarPath, int]] = [(p, optimal_score(p)) for p in i.paths]
    path_and_scores = sorted(path_and_scores, key=lambda x: x[1], reverse=True)

    counts_in_streets_by_intersection_id: Dict[int, Dict[Street, int]] = defaultdict(lambda: defaultdict(lambda: 0))
    counts_by_intersection: Dict[int, int] = defaultdict(lambda: 0)

    for path, score in path_and_scores:
        for street in path.streets:
            counts_in_streets_by_intersection_id[street.end][street] += score

    for intersection_id, score_by_street in counts_in_streets_by_intersection_id.items():
        total_period_duration = len(score_by_street) * 2
        total_score = sum(score_by_street.values())
        compute_time = lambda count: int(count * total_period_duration // total_score)
        green_lights: Dict[Street, int] = {s: max(1, compute_time(c)) for s, c in score_by_street.items()}

        print("-"*100)
        print(total_period_duration)
        print(sorted(green_lights.values()))

        schedule = Schedule(intersection_id=intersection_id, green_light_streets=green_lights)
        schedules.append(schedule)

    return Output(tuple(schedules))