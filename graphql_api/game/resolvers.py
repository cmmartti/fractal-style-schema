from .. import data


def characters(root, info):
    return [c for c in data.characters if root.id in c.games]

def all_games(root, info):
    return data.games
