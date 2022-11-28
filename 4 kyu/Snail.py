def snail(array):
    answer = []
    while len(array) > 0:
        answer += array[0]
        del array[0]

        if len(array) > 0:
            for i in array:
                answer += [i[-1]]
                del i[-1]

            answer += array[-1][::-1]
            del array[-1]

            for i in reversed(array):
                answer += [i[0]]
                del i[0]

    return answer