import base64

__all__ = [
    'generate_key',
    'apply_fault'
]


def generate_key(*args):
    if args and len(args) and args != (None,):
        result = '-'.join([str(arg) for arg in args if arg is not None])
        return base64.b64encode(str.encode(result))
    else:
        return None


def apply_fault(method, x, value):
    return value
