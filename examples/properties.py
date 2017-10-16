import datetime

import goblin
from gremlin_python.statics import long


class DateTime(goblin.abc.DataType):

    def validate(self, val):
        if not isinstance(val, datetime.datetime):
            raise goblin.exception.ValidationError(
                "Not a valid datetime.datetime: {}".format(val))
        return val

    def to_ogm(self, val):
        return super().to_ogm(val)

    def to_db(self, val):
        return super().to_db(val)


class Long(goblin.properties.Integer):
    """No long/int distinction in Python 3"""
    def to_db(self, val):
        # Make sure to serialize as long
        if val is not None:
            return long(val)
