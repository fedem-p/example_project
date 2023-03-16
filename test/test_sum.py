import sys

sys.path.insert(0, "/home/fpuppo/workspace/example_project/core")

from my_project import my_sum
import pytest
import random


@pytest.fixture
def my_fixture():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    return (a, b, a + b)


@pytest.mark.parametrize(
    "a,b, expected_output", [(3, 4, "9"), (0, 0, 3), (3, 4, 7), (0, 0, 0)]
)
def test_my_sum(a, b, expected_output):
    assert my_sum(a, b) == expected_output
