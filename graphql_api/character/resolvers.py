from .. import data


def games(root, info):
    return [g for g in data.games if g.id in data.characters[root.id].games]

def all_characters(root, info):
    return data.characters
