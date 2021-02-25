#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Dataset summary."""

import argparse
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

import numpy as np

from hashcode.common.base import Input, read_input
from hashcode.common.model import Street

parser = argparse.ArgumentParser(
    "hashcode",
    description="CLI utility for Google Hash Code. "
    "It assumes the input provided in stdin.",
)

parser.add_argument(
    "--in", dest="in_file", type=str, default=None, help="provide an input data file."
)
args = parser.parse_args()


def print_stats(data, label):
    """Print statistics."""
    print("Avg {}: {}".format(label, np.mean(data)))
    print("Std {}: {}".format(label, np.std(data)))
    print("Max {}: {}".format(label, np.max(data)))
    print("Min {}: {}".format(label, np.min(data)))
    print("00th {}: {}".format(label, np.percentile(data, 0)))
    print("25th {}: {}".format(label, np.percentile(data, 25)))
    print("50th {}: {}".format(label, np.percentile(data, 50)))
    print("75th {}: {}".format(label, np.percentile(data, 75)))
    print("100th {}: {}".format(label, np.percentile(data, 100)))
    print("-" * 50)


def print_intersection_stats(i: Input):

    nb_input_streets = []
    nb_output_streets = []
    for intersection_ in i.intersections.values():
        nb_input_streets.append(len(intersection_.in_streets))
        nb_output_streets.append(len(intersection_.out_streets))

    print(f"Avg nb input streets in intersections: {np.mean(nb_input_streets)}")
    print(f"Std nb input streets in intersections: {np.std(nb_input_streets)}")
    print(f"Max nb input streets in intersections: {np.max(nb_input_streets)}")
    print(f"Min nb input streets in intersections: {np.min(nb_input_streets)}")

    print("*"*10)

    print(f"Avg nb output streets in intersections: {np.mean(nb_output_streets)}")
    print(f"Std nb output streets in intersections: {np.std(nb_output_streets)}")
    print(f"Max nb output streets in intersections: {np.max(nb_output_streets)}")
    print(f"Min nb output streets in intersections: {np.min(nb_output_streets)}")


if __name__ == "__main__":
    input_: Input = read_input(Path(args.in_file).open())

    print(f"Nb cars: {len(input_.paths)}")
    print(f"Nb streets: {len(input_.streets)}")
    print(f"Nb intersections: {input_.nb_intersections}")
    print(f"Duration: {input_.duration_seconds}")
    print(f"Bonus: {input_.bonus_points}")
    print("*"*10)
    print(f"Avg path length: {np.mean([p.length for p in input_.paths])}")
    print(f"Std path length: {np.std([p.length for p in input_.paths])}")
    print(f"Max path length: {np.max([p.length for p in input_.paths])}")
    print(f"Min path length: {np.min([p.length for p in input_.paths])}")
    print("*" * 10)
    print_intersection_stats(input_)
