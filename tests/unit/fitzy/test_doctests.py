import doctest
import os.path
from importlib import import_module
from pathlib import Path
from typing import Iterable

import pytest


def find_doctest_contained_modules() -> Iterable[str]:
    def remove_suffix(string: str, suffix: str) -> str:
        return string[: -len(suffix)]

    def path_to_module(path: str) -> str:
        return path.replace(os.path.sep, ".")

    for path in Path("src").glob("**/*.py"):
        if ">>>" in path.read_text():
            yield path_to_module(remove_suffix(str(path.relative_to("src")), ".py"))


@pytest.mark.parametrize("module_name", find_doctest_contained_modules())
def test_modules_doctests(module_name: str) -> None:
    # Arrange
    module = import_module(module_name)

    # Act
    test_results = doctest.testmod(module)

    # Assert
    assert test_results.attempted
    assert not test_results.failed
