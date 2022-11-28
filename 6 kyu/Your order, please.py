def my_key(word: str):
    for i in word:
        if i.isdigit():
            return int(i)


def order(sentence):
    return ' '.join(sorted(sentence.split(), key=my_key))
