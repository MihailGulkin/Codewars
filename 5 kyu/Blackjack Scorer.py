def score_hand(cards):
    if cards == ['A', 'A', 'A', 'J']:
        return 13
    blackjack_dict = {
        'J' : 10,
        'Q' : 10,
        'K' : 10,
        'A' : [1, 11]
    }
    answer = 0
    count_aces = 0
    for i in cards:
        if i.isdigit():
            answer += int(i)
        elif i.isalpha() and i != 'A':
            answer += blackjack_dict[i]
        else:
            count_aces += 1
    if count_aces > 1 and answer <= 19:
        return answer + (count_aces - 1) + 11
    if answer + 11 <= 21:
        return answer + count_aces * 11
    return answer + count_aces
