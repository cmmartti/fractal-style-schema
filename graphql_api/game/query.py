
from graphene import List

from ..base import BaseQuery
from ..data import games
from .types import Game

class Query(BaseQuery):
    games = List(lambda: Game, description="A list of video games.")

    def resolve_games(self, info):
        return games
