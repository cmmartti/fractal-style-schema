
class Game(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Character(object):
    def __init__(self, id, name, games):
        self.id = id
        self.name = name
        self.games = games


games = [
    Game(id=0, name="The Legend of Zelda: Wind Waker"),
    Game(id=1, name="The Legend of Zelda: Phantom Hourglass"),
    Game(id=2, name="Super Mario"),
    Game(id=3, name="Mario Kart"),
    Game(id=4, name="MegaMan"),
    Game(id=5, name="Super Smash Bros"),
]

characters = [
    Character(id=0, name="Mario", games=[2, 3, 5]),
    Character(id=1, name="Bowser", games=[2, 3, 5]),
    Character(id=2, name="Link", games=[0, 1, 5]),
    Character(id=3, name="Zelda", games=[0, 1, 5]),
    Character(id=4, name="MegaMan", games=[4, 5]),
]

def get_characters_for_game(id):
    return [c for c in characters if id in c.games]

def get_games_for_character(id):
    return [g for g in games if g.id in characters[id].games]
