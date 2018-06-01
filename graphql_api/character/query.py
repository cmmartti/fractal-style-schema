
from graphene import List

from ..data import characters
from ..base import BaseQuery
from .types import Character

class Query(BaseQuery):
    characters = List(lambda: Character, description="A list of video game characters.")

    def resolve_characters(self, info):
        return characters
