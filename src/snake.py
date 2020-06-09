class Snake:
    id: str
    name: str
    health: int
    body: list
    head: dict
    length: int

    def __init__(self, data):
        self.update(data)
    
    def update(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.health = data["health"]
        self.body = data["body"]
        self.head = data["head"]
        self.length = data["length"]

class Board:
    width: int
    height: int
    food: list
    snakes: list

    def __init__(self, data):
        pass

    def update_all(self, data):
        self.width = data["width"]
        self.height = data["height"]
        self.food = data["food"]
        self.snakes = []

        for i in data["snakes"]:
            self.snakes.append(Snake(i))

tylers = {}

def start(data):
    tylers[data['game']['id']] = Snake(data['you'])

def clear(data):
    del tylers[data['game']['id']]

def update(data):
    tyler = tylers[data['game']['id']]
    tyler.update(data['you'])

def move(data):
    return "left"