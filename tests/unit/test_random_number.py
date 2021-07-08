from src.use_cases.random_number import get_random_number


def test_get_random_number():
    number = get_random_number()
    assert 100 >= number >= 1
