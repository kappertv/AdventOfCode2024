from src.day02.solution import *

import pytest
import os

@pytest.fixture
def sampleinput():
    return os.path.join(os.path.dirname(__file__), "resources", "day02sampleinput.txt")

def test_numberOfSafeReports(sampleinput):
    assert numberOfSafeReports(sampleinput) == 2

def test_numberOfSafeReportsPart2(sampleinput):
    assert numberOfSafeReportsDamped(sampleinput) == 4

@pytest.fixture
def input():
    return os.path.join(os.path.dirname(__file__), "resources", "day02input.txt")

def test_numberOfSafeReportsInput(input):
    assert numberOfSafeReports(input) == 218

def test_numberOfSafeReportsPart2Input(input):
    assert numberOfSafeReportsDamped(input) == 290
