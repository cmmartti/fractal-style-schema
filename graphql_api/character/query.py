from graphene import List

from ..base import BaseQuery
from .types import Character
from . import resolvers as resolve


class Query(BaseQuery):
    characters = List(
        lambda: Character,
        description="A list of video game characters.",
        resolver=resolve.all_characters
    )
