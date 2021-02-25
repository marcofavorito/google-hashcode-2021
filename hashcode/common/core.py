# -*- coding: utf-8 -*-
"""Core module of the framework."""
import importlib

from hashcode.common.base import Input, Output


class Solution:
    """
    This class acts as a wrapper for solution modules in 'hashcode/solutions'.

    It dynamically imports the module and ensures
    that the solution module contains a 'main' function.
    """

    def __init__(self, module_name: str):
        """
        Initialize the solution wrapper.

        :param module_name: name of the module.
        """
        self._module_name = module_name
        self._module_dotted_path = f"hashcode.solutions.{module_name}"
        self.module = importlib.import_module(self._module_dotted_path)
        self._check_consistency()

    def main(self, i: Input) -> Output:
        """Run the solution on an Input and produce an Output."""
        output = self.module.main(i)  # type: ignore
        return output

    def _check_consistency(self):
        """Check the consistency of the dynamically loaded module."""
        fun = getattr(self.module, "main", None)
        is_callable = callable(fun) if fun else False
        if is_callable:
            raise ValueError(
                f"Module {self._module_dotted_path} does not have a callable named 'main'."
            )
