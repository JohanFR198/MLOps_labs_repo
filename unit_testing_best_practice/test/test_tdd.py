import sys
import os

# Add src directory to path using absolute path from this file's location
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


from class_2_tdd import isprime



def test_isprime():
    assert isprime(2)
    assert isprime(3)
    assert not isprime(4)
    assert isprime(5)
    assert not isprime(12)
    assert not isprime(25)
    assert isprime(29)
    