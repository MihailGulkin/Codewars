def duplicate_count(text):
    return sum(1 for i in set(text.lower()) if text.lower().count(i) > 1)
