from app import app, loop
from models import House, Structure, BranchesTo


async def create_graph():
    pass


loop.run_until_complete(app.close())
