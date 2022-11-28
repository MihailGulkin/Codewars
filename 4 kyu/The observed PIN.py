def get_pins(observed):
    _dict = {
        1: [1, 2, 4],
        2: [1, 2, 3, 5],
        3: [2, 3, 6],
        4: [1, 5, 4, 7],
        5: [2, 5, 6, 4, 8],
        6: [3, 5, 9, 6],
        7: [4, 8, 7],
        8: [5, 9, 7, 0, 8],
        9: [6, 8, 9],
        0: [0, 8]
    }
    _list = []
    if len(observed) == 1:
        for i in _dict[int(observed)]:
            _list.append(str(i))
        return _list
    elif len(observed) == 2:
        for i in _dict[int(observed[0])]:
            for j in _dict[int(observed[1])]:
                _list.append(str(i) + str(j))
        return _list
    elif len(observed) == 3:
        for i in _dict[int(observed[0])]:
            for j in _dict[int(observed[1])]:
                for k in _dict[int(observed[2])]:
                    _list.append(str(i) + str(j) + str(k))
        return _list
    elif len(observed) == 4:
        for i in _dict[int(observed[0])]:
            for j in _dict[int(observed[1])]:
                for k in _dict[int(observed[2])]:
                    for d in _dict[int(observed[3])]:
                        _list.append(str(i) + str(j) + str(k) + str(d))
        return _list
    elif len(observed) == 8:
        for i in _dict[int(observed[0])]:
            for j in _dict[int(observed[1])]:
                for k in _dict[int(observed[2])]:
                    for d in _dict[int(observed[3])]:
                        for l in _dict[int(observed[4])]:
                            for m in _dict[int(observed[5])]:
                                for v in _dict[int(observed[6])]:
                                    for c in _dict[int(observed[7])]:
                                        _list.append(
                                            str(i) + str(j) + str(k) + str(
                                                d) + str(l) + str(m) + str(
                                                v) + str(c))
        return _list
