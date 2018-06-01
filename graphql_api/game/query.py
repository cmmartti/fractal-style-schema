from graphene import List

from ..base import BaseQuery
from .types import Game
from . import resolvers as resolve


class Query(BaseQuery):
    games = List(
        lambda: Game,
        description="A list of video games.",
        resolver=resolve.all_games
    )
