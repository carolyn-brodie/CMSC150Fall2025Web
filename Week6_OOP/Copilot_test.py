def add_numbers():
    """
    Add numbers between 1 and 10 (inclusive).
    >>> add_numbers()
    55
    """
    total = 0
    for number in range(1, 11):
        total += number
    return total
