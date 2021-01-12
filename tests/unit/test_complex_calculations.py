from src.use_cases.complex_calculations import calculate_something


def test_calculate_something():
    assert calculate_something() == 4
