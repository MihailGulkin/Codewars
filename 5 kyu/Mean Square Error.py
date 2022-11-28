def solution(array_a, array_b):
    answer = 0
    for i in range(len(array_a)):
        answer += (abs(array_a[i] - array_b[i]) ** 2)
    return answer / len(array_a)
