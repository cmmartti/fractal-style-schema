from graphene import ObjectType, Int, String, List
from ..data import get_characters_for_game

# from ..character.types import Character

class Game(ObjectType):
    id = Int()
    name = String(description="The name of this video game.")
    # characters = List(lambda: Character, description="Characters in this video game.")

    # def resolve_characters(self, info):
    #     return get_characters_for_game(self.id)
