from src.day07.solution import *

import pytest
import os

@pytest.fixture
def sampleinput():
    return os.path.join(os.path.dirname(__file__), "resources", "day07sampleinput.txt")

def test_part2(sampleinput):
    assert part1(sampleinput) == 11387

@pytest.fixture
def input():
    return os.path.join(os.path.dirname(__file__), "resources", "day07input.txt")

def test_part2i(input):
    assert part1(input) == 472290821152397