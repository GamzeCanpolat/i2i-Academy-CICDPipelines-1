from app import calculate_telecom_tax


def test_calculate_telecom_tax():
    assert calculate_telecom_tax(100) == 10