__all__ = [
    'dict_get_or_else',
    'get_first_not_none'
]


def dict_get_or_else(d, key, else_value=None):
    if d is None:
        return else_value
    if key in d:
        return d[key]
    else:
        return else_value


def get_first_not_none(*args):
    for arg in args:
        if arg is not None:
            return arg
    return None
