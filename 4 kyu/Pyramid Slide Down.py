def longest_slide_down(pyramid):
    for i in reversed(range(len(pyramid) - 1)):
        for j in range(len(pyramid[i])):
            pyramid[i][j] += max(pyramid[i + 1][j], pyramid[i + 1][j + 1])
    return pyramid[0][0]
