from src.day09.solution import *

import pytest
import os

@pytest.fixture
def sampleinput():
    return os.path.join(os.path.dirname(__file__), "resources", "day09sampleinput.txt")

def test_part1(sampleinput):
    assert part1_checksum(sampleinput) == 1928

@pytest.fixture
def input():
    return os.path.join(os.path.dirname(__file__), "resources", "day09input.txt")

def test_part1i(input):
    assert part1_checksum(input) == 1928 # too low 90180292337