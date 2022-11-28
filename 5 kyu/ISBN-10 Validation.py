def valid_ISBN10(isbn):
    if len(isbn) != 10:
        return False
    try:
        isbn = list(isbn)
        isbn[-1] = '10' if isbn[-1] == 'X' else isbn[-1]
        answer = 0
        for i in range(len(isbn)):
            answer += (int(isbn[i]) * (i + 1))
        return answer % 11 == 0
    except:
        return False
