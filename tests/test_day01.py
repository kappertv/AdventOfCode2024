from src.day01.solution import *

import pytest
import os

@pytest.fixture
def sampleinput():
    return os.path.join(os.path.dirname(__file__), "resources", "day01sampleinput.txt")

def test_part1(sampleinput):
    assert part1(sampleinput) == 11

@pytest.fixture
def input():
    return os.path.join(os.path.dirname(__file__), "resources", "day01input.txt")

def test_part1_input(input):
    assert part1(input) == 765748

def test_part2_sampleinput(sampleinput):
    assert similarityScore(sampleinput) == 31

def test_part2_input(input):
    assert similarityScore(input) == 27732508
