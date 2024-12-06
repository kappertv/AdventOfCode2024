from src.day06.solution import *

import pytest
import os

@pytest.fixture
def sampleinput():
    return os.path.join(os.path.dirname(__file__), "resources", "day06sampleinput.txt")

def test_part1(sampleinput):
    assert part1(sampleinput) == 41

def test_part2(sampleinput):
    assert part2(sampleinput) == 6

@pytest.fixture
def input():
    return os.path.join(os.path.dirname(__file__), "resources", "day06input.txt")

def test_part1i(input):
    assert part1(input) == 4696
