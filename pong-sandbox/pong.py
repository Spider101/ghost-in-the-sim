import pygame
WIDTH, HEIGHT = 500, 500 

class Ball:
    def __init__(self, difficulty, willMoveLeft):
        self.coords = [ WIDTH // 2, HEIGHT // 2 ]
        self._radius = 10 
        self._init_vel = [-2 if willMoveLeft else 2, -2]
        self._speed_boost = difficulty
        self.velocity = self.initial_velocity

    @property
    def radius(self):
        return self._radius

    @property
    def initial_velocity(self):
        return self._init_vel

    @property
    def speed_boost(self):
        return self._speed_boost

    def reset(self):
        self.coords = [ WIDTH // 2, HEIGHT // 2 ]
        self.velocity = self.initial_velocity

    def update_coords(self, paddles):
        paddle_gutters = sorted([paddles[0].gutter_boundary, paddles[1].gutter_boundary])
        paddle_offsets = [-1 * paddles[0].height // 2, paddles[0].height // 2]
        paddle_hitboxes = [ [ paddle.y_pos + offset for offset in paddle_offsets ] for paddle in paddles ]

        x, y = [ coord + vel for coord, vel in zip(self.coords, self.velocity) ]

        if x - self.radius <= paddle_gutters[0] or x + self.radius >= paddle_gutters[1]:
            if (paddle_hitboxes[0][0] <= y <= paddle_hitboxes[0][1]
                or paddle_hitboxes[1][0] <= y <= paddle_hitboxes[1][1]):
                self.velocity = [ vel * self.speed_boost for vel in self.velocity ]
                self.velocity[0] *= -1
            else:
                self.reset()

        elif y + self.radius >= HEIGHT or y - self.radius <= 0:
            self.velocity[1]  *= -1

        self.coords = [ coord + vel for coord, vel in zip(self.coords, self.velocity)]

    def draw(self, window):
        pygame.draw.circle(window, (255, 255, 255), self.coords, self.radius)

class Player:
    def __init__(self, isTurn, alias):
        self.isTurn = isTurn
        self.score = 0
        self.paddle = Paddle(isTurn)
        self.name = alias

class Paddle:
    def __init__(self, isLeft):
        self._vel = -4
        self._height = 40
        self._width = 10
        self._gutter_boundary = self.width if isLeft else WIDTH - self.width
        self.y_pos = (HEIGHT - self.height ) // 2
        self._x_pos = 0 if isLeft else WIDTH - self.width

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    @property
    def x_pos(self):
        return self._x_pos

    @property
    def velocity(self):
        return self._vel

    @property
    def gutter_boundary(self):
        return self._gutter_boundary

    def update_coords(self, sign):
        y = self.y_pos + sign * self.velocity
        wall_gutters = [ 0, HEIGHT - self.height ]
        if wall_gutters[0] < y < wall_gutters[1]:
            self.y_pos = y
        elif y < wall_gutters[0]:
            self.y_pos = wall_gutters[0]
        elif y > wall_gutters[1]:
            self.y_pos = wall_gutters[1] 

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), (self.x_pos, self.y_pos, self.width, self.height))
