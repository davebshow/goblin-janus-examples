from app import app, loop
from models import House, Structure, BranchesTo


async def test_query():
    session = await app.session()
    house = House()
    house.string_prop = ['7986', '87236']
    house = await session.save(house)
    assert house.string_prop[-1].value == '87236'
    vp = await session.g.V().hasLabel(
        'house').properties('string_prop').hasValue('87236').toList()
    print("this is the vertex prop: {}".format(vp))
    v = await session.g.V().hasLabel('house').has('string_prop', '87236').next()
    print("this is the vertex {} with props: {}".format(v, v.string_prop))

loop.run_until_complete(test_query())
loop.run_until_complete(app.close())
