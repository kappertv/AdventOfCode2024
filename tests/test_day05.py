from src.day05.solution import *

import pytest
import os

@pytest.fixture
def sampleinput():
    return os.path.join(os.path.dirname(__file__), "resources", "day05sampleinput.txt")

def test_sumOfMultiplications(sampleinput):
    assert part1(sampleinput) == 143

def test_part2(sampleinput):
    assert part2(sampleinput) == 123

@pytest.fixture
def input():
    return os.path.join(os.path.dirname(__file__), "resources", "day05input.txt")

def test_sumOfMultiplicationsInput(input):
    assert part1(input) == 4609

def test_part2Input(input):
    assert part2(input) == 5723
