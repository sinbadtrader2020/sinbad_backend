import datetime

class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)


def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()