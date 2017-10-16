import datetime
from examples.app import app, loop
from examples.models import House


async def test_query():
    session = await app.session()
    # Drop any existing verts/edges
    await session.g.V().drop().iterate()
    await session.g.E().drop().iterate()
    # Create a vertex with a VP with metas
    house = House()
    house.string_prop = '87236'
    house.string_prop.notes = 'This is a string'
    house.string_prop.datetime = datetime.datetime.now()
    house = await session.save(house)
    assert house.string_prop.value == '87236'

    # Get a new session from goblin to confirm vertex was created in janus with metas
    session = await app.session()
    vp = await session.g.V().hasLabel(
        'house').properties('string_prop').hasValue('87236').toList()
    print("this is the vertex prop: {}".format(vp))
    v = await session.g.V().hasLabel('house').has('string_prop', '87236').next()
    print("this is the vertex {} with props {} and metas notes '{}' and datetime '{}'".format(v, v.string_prop,
                                                                                              v.string_prop.notes,
                                                                                              v.string_prop.datetime))

loop.run_until_complete(test_query())
loop.run_until_complete(app.close())
