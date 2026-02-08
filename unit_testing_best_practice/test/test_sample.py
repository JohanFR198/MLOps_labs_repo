import sys
import os

# Add src directory to path using absolute path from this file's location
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from sample import *

def test_answer():
    assert func(3) == 5