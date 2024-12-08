from src.day04.solution import *

import pytest
import os

@pytest.fixture
def sampleinput():
    return os.path.join(os.path.dirname(__file__), "resources", "day04sampleinput.txt")

def test_part1_numberOfXMAS(sampleinput):
    assert part1(sampleinput) == 18

def test_part2_numberOfX_MAS(sampleinput):
    assert part2(sampleinput) == 9

@pytest.fixture
def input():
    return os.path.join(os.path.dirname(__file__), "resources", "day04input.txt")

def test_part1_numberOfXMASi(input):
    assert part1(input) == 2644

def test_part2_numberOfX_MASi(input):
    assert part2(input) == 1952
