def get_count(sentence):
    return sum([sentence.count(i) for i in 'aeiou'])
