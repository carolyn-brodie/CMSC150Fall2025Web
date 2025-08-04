def sum_numbers_between_1_and_n(n):
    """
    Add numbers between 1 and n (inclusive).
    :param n: int
    :return: int the sum
    >>> sum_numbers_between_1_and_n(10)
    55
    >>> sum_numbers_between_1_and_n(100)
    5050
    """
    total = 0
    for number in range(1, n+1):
        total += number
    return total

# result = sum_numbers_between_1_and_10()
# print(result)


list1 = []
list1.append(2)