def solution(string, ending):
    return string[-len(ending):] == ending if ending != '' else True

