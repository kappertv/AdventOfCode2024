from src.day0.solution import *

import pytest
import os

@pytest.fixture
def input():
    return os.path.join(os.path.dirname(__file__), "resources", "day00input.txt")

def test_part1(input):
    assert part1(input) == 70296

def test_part2(input):
    assert part2(input) == 205381