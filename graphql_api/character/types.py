from graphene import ObjectType, Int, String, List
from ..data import get_games_for_character
from ..game.types import Game

class Character(ObjectType):
    id = Int()
    name = String(description="The name of this character.")
    games = List(lambda: Game, description="Video games this character is in.")

    def resolve_games(self, info):
        return get_games_for_character(self.id)
