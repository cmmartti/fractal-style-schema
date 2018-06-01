from graphene import ObjectType, Int, String, List, lazy_import

from . import resolvers as resolve


class Game(ObjectType):
    """A video game."""

    id = Int()
    name = String(description="The name of this video game.")
    characters = List(
        lazy_import("graphql_api.character.types.Character"),
        description="Characters in this video game.",
        resolver=resolve.characters
    )
