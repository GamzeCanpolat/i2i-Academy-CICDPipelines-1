def calculate_telecom_tax(amount):
    """
    Calculates 10% telecom tax for a given amount.
    """
    if amount < 0:
        raise ValueError("Amount cannot be negative")

    return amount * 0.10