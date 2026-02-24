import sys
import os

# Add src directory to path using absolute path from this file's location
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from sample import *

def test_answer():
    assert func(3) == 5



def test_validate_username():
    assert validate_username("john_doe")
    assert not validate_username("")
    assert not validate_username("john doe")


def test_validate_password():
    assert validate_password("Passw0rd!")
    assert not validate_password("short1!")
    assert not validate_password("password!")
    assert not validate_password("Password1")
    assert not validate_password("12345678!")


def test_validate_email():
    assert validate_email("test@example.com")
    assert not validate_email("testexample.com")
    assert not validate_email("test@examplecom")


def test_calculate_area():
    assert calculate_area(5) == 78.53981633974483
    assert calculate_area(0) == 0
    assert calculate_area(-1) == 0
