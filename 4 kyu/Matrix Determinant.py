import numpy as np
from math import ceil


def determinant(matrix):
    answer = np.linalg.det(np.array(matrix))
    answer = str(answer)
    print()
    if float(answer) > 0:
        if int(answer[answer.find('.') + 1:answer.find('.') + 2]) > 5:
            return ceil(float(answer))
        return int(float(answer))
    else:
        if int(answer[answer.find('.') + 1:answer.find('.') + 2]) > 5:
            return int(float(answer) - 1)
        return int(float(answer))
