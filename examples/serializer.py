import datetime
from gremlin_python.driver import serializer
from gremlin_python.structure.io import graphson


class DateSerializer:

    def dictify(self, obj, writer):
        # Java timestamp expects miliseconds
        ts = round(obj.timestamp() * 1000)
        return graphson.GraphSONUtil.typedValue('Date', ts)


class DateDeserializer:

    def objectify(self, ts, reader):
        # Python timestamp expects seconds
        dt = datetime.datetime.fromtimestamp(ts / 1000.0)
        return dt


reader = graphson.GraphSONReader({'g:Date': DateDeserializer()})
writer = graphson.GraphSONWriter({datetime.datetime: DateSerializer()})

message_serializer = serializer.GraphSONMessageSerializer(reader=reader,
                                                          writer=writer)
