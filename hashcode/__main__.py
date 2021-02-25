#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main entrypoint of the framework.

To print the usage:

    python -m hashcode --help

"""

import inspect
import logging
import os
import re
import sys
from pathlib import Path

import click

from hashcode.common.base import Input, Output, read_input, score, write_output
from hashcode.common.core import Solution

logger = logging.getLogger("hashcode")

PACKAGE_DIRECTORY = os.path.dirname(inspect.getfile(inspect.currentframe()))  # type: ignore
ALGORITHMS = sorted(
    [
        s.stem
        for s in Path(PACKAGE_DIRECTORY + "/solutions").iterdir()
        if re.match("[^_].+.py", s.name)
    ]
)


@click.command("hashcode", help="CLI util for Google Hash Code <year>.")
@click.option(
    "--alg",
    required=True,
    type=click.Choice(ALGORITHMS),
    help="The algorithm to use for computing the solution.",
)
@click.option(
    "-i",
    "--in_",
    default=None,
    type=click.Path(exists=True, dir_okay=False, readable=True),
    help="Provide an input data file. Defaults to stdin",
)
@click.option(
    "-o",
    "--out",
    default=None,
    type=click.Path(exists=False, dir_okay=False, writable=True),
    help="Provide an output data file. Defaults to stdout",
)
def main(alg: str, in_, out):
    """Run a solution against a problem instance."""
    input_stream = Path(in_).open() if in_ else sys.stdin
    output_stream = Path(out).open("w") if out else sys.stdout

    solution = Solution(alg)

    logger.debug(f"Chosen algorithm: {alg}")
    input_: Input = read_input(input_stream)
    output: Output = solution.main(input_)
    solution_score = score(input_, output)
    logger.debug(f"Score of the solution: {solution_score}")
    write_output(output, output_stream)


if __name__ == "__main__":
    main()
