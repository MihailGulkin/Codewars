def variance(numbers):
    mean = sum(numbers) / len(numbers)
    answer = 0
    for i in numbers:
        answer += (i - mean) ** 2
    return answer / len(numbers)