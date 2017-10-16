import asyncio
import goblin
from aiogremlin import Cluster

from examples import models
from examples.serializer import message_serializer


def get_hashable_id(val):
  if isinstance(val, dict) and "@type" in val and "@value" in val:
      if val["@type"] == "janusgraph:RelationIdentifier":
          val = val["@value"]["value"]
  return val


loop = asyncio.get_event_loop()


cluster = loop.run_until_complete(
    Cluster.open(loop, message_serializer=message_serializer))


app = goblin.Goblin(cluster, get_hashable_id=get_hashable_id)

app.register_from_module(models)


