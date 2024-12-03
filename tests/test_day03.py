from src.day03.solution import *

import pytest
import os

@pytest.fixture
def sampleinput():
    return os.path.join(os.path.dirname(__file__), "resources", "day03sampleinput.txt")

def test_sumOfMultiplications(sampleinput):
    assert getSumOfMultiplications(sampleinput) == 161

@pytest.fixture
def sampleinputpart2():
    return os.path.join(os.path.dirname(__file__), "resources", "day03sampleinputpart2.txt")

def test_sumOfMultiplicationsPart2(sampleinputpart2):
    assert getSumOfMultiplicationsPart2(sampleinputpart2) == 48

@pytest.fixture
def input():
    return os.path.join(os.path.dirname(__file__), "resources", "day03input.txt")

def test_sumOfMultiplicationsInput(input):
    assert getSumOfMultiplications(input) == 184122457

def test_sumOfMultiplicationsPart2Input(input):
    assert getSumOfMultiplicationsPart2(input) == 107862689
