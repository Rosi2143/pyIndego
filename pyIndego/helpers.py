from dataclasses import dataclass
from dataclasses import is_dataclass
from datetime import datetime

def nested_dataclass(*args, **kwargs):
    def wrapper(cls):
        cls = dataclass(cls, **kwargs)
        original_init = cls.__init__

        def __init__(self, *args, **kwargs):
            for name, value in kwargs.items():
                field_type = cls.__annotations__.get(name, None)
                if is_dataclass(field_type) and isinstance(value, dict):
                    new_obj = field_type(**value)
                    kwargs[name] = new_obj
            original_init(self, *args, **kwargs)

        cls.__init__ = __init__
        return cls

    return wrapper(args[0]) if args else wrapper


def convert_bosch_datetime(boschdatetime=None):
    if boschdatetime:
        tmp = '{:%Y-%m-%d %H:%M}'.format(datetime.fromisoformat(boschdatetime))
        return tmp
    return None
