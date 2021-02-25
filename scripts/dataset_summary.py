#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Dataset summary."""

import argparse
from pathlib import Path

import numpy as np

from hashcode.common.base import Input, read_input

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


if __name__ == "__main__":
    input_: Input = read_input(Path(args.in_file).open())

    print(f"Nb cars: {len(input_.paths)}")
    print(f"Nb streets: {len(input_.streets)}")
    print(f"Avg path length: {np.mean([p.length for p in input_.paths])}")
    print(f"Std path length: {np.std([p.length for p in input_.paths])}")