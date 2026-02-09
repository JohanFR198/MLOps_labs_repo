def validate_isprime():
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(12)
    assert not is_prime(25)
    assert is_prime(29)
    