from graphene import ObjectType, Int, String, List, lazy_import

from . import resolvers as resolve


class Character(ObjectType):
    """A character from a video game."""

    id = Int()
    name = String(description="The name of this character.")
    games = List(
        lazy_import("graphql_api.game.types.Game"),
        description="Video games this character is in.",
        resolver=resolve.games
    )
