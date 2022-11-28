def sum_two_smallest_numbers(numbers):
    first_min = min(numbers)
    numbers.pop(numbers.index(first_min))
    return first_min + min(numbers)
