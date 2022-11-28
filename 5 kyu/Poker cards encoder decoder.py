card = 'A23456789TJQK'


def encode(cards):
    card_c = {}
    card_d = {}
    card_h = {}
    card_s = {}
    big_deck = [
        card_c, card_d, card_h, card_s
    ]
    count = 0
    for i in range(0, 52):
        if count == 13:
            count = 0
            big_deck.pop(0)
        big_deck[0][card[count]] = i
        count += 1
    answ_list = []
    for ele in cards:
        if 'c' in ele:
            answ_list.append(card_c[ele.replace('c', '')])
        if 'd' in ele:
            answ_list.append(card_d[ele.replace('d', '')])
        if 'h' in ele:
            answ_list.append(card_h[ele.replace('h', '')])
        if 's' in ele:
            answ_list.append(card_s[ele.replace('s', '')])
    return sorted(answ_list)


def decode(cards):
    big_deck = {

    }
    count = 0
    suits = ['c', 'd', 'h', 's']
    for i in range(0, 52):
        if count == 13:
            count = 0
            suits.pop(0)
        big_deck[i] = card[count] + suits[0]
        count += 1
    answer_list = []
    for ele in sorted(cards):
        answer_list.append(big_deck[ele])
    return answer_list
