def search_substr(full_text, search_text, allow_overlap=True):
    if len(full_text) == 0 or len(search_text) == 0:
        return 0
    if not allow_overlap:
        return full_text.count(search_text)
    else:
        count = start = 0
        while True:
            start = full_text.find(search_text, start) + 1
            if start > 0:
                count+=1
            else:
                return count