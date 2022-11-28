def create_class(class_name, secrets=None):
    if secrets is None:
        secrets = {"__init__": 3}
    if class_name == '':
        return None
    return type(class_name, (object,), secrets)
