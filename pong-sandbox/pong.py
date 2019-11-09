WIDTH, HEIGHT = 500, 500 

class Ball:
    def __init__(self, difficulty):
        self.coords = [WIDTH / 2, HEIGHT / 2]
        self._radius = 50
        self._vel = 2
        self._speed_boost = difficulty

    @property
    def radius(self):
        return self._radius

    @property
    def velocity(self):
        return self._vel

    @property
    def speed_boost(self):
        return self._speed_boost

    def update_coords(self):
        pass

class Player:
    def __init__(self, isTurn, alias):
        self.isTurn = isTurn
        self.score = 0
        self.paddle = Paddle(isTurn)
        self.name = alias

class Paddle:
    def __init__(self, isLeft):
        self._vel = 2
        self._height = 20
        self._width = 5
        self.coords = (0, HEIGHT / 2 - self._height / 2) if isLeft else (WIDTH - self._width, HEIGHT / 2 - self._height / 2)

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    @property
    def velocity(self):
        return self._vel

    def update_coords(self):
        pass
