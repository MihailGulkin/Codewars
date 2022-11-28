def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        for i in pin:
            if not i.isnumeric():
                return False
        return True
    return False
