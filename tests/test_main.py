from src.main import hello_world

def test_hello_world():
    assert hello_world() == "Hello, World!"

import os
import pytest
from src.main import process_file

@pytest.fixture
def input_file_path():
    # Zorgt dat het pad altijd relatief is ten opzichte van dit script
    return os.path.join(os.path.dirname(__file__), "resources", "day00expectedresult.txt")

def test_process_file(input_file_path):
    result = process_file(input_file_path)
    assert result == "EXPECTED RESULT"