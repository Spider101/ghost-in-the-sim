import pygame

class Pong:
    def __init__(self, player_names):
        self._screen_dims = [ 500, 500 ]
        self.ball = Ball(1, self.screen_dims)
        self.player1 = Player(True, player_names[0], self.screen_dims)
        self.player2 = Player(False, player_names[1], self.screen_dims)
        self.scores = []
    
    @property
    def screen_dims(self):
        return self._screen_dims

    def update_ball_coords(self):
        paddles = [self.player1.paddle, self.player2.paddle]
        paddle_gutters = sorted([paddles[0].gutter_boundary, paddles[1].gutter_boundary])
        paddle_offsets = [-1 * paddles[0].height // 2, paddles[0].height // 2]
        paddle_hitboxes = [ [ paddle.y_pos + offset for offset in paddle_offsets ] for paddle in paddles ]

        x, y = [ coord + vel for coord, vel in zip(self.ball.coords, self.ball.velocity) ]

        if x - self.ball.radius <= paddle_gutters[0] or x + self.ball.radius >= paddle_gutters[1]:
            if (paddle_hitboxes[0][0] <= y <= paddle_hitboxes[0][1]
                or paddle_hitboxes[1][0] <= y <= paddle_hitboxes[1][1]):
                self.ball.velocity = [ vel * self.ball.speed_boost for vel in self.ball.velocity ]
                self.ball.velocity[0] *= -1
            else:
                self.ball.reset(self.screen_dims)

        elif y + self.ball.radius >= self.screen_dims[1] or y - self.ball.radius <= 0:
            self.ball.velocity[1]  *= -1

        self.ball.coords = [ coord + vel for coord, vel in zip(self.ball.coords, self.ball.velocity)]
    
    def update_player_coords(self, player, direction):
        player.update_paddle_coords(self.screen_dims[1], direction)
    
    def draw(self, window):
        self.ball.draw(window)
        self.player1.paddle.draw(window)
        self.player2.paddle.draw(window)

class Ball:
    def __init__(self, difficulty, screen_dims):
        width, height = screen_dims
        self.coords = [ width // 2, height // 2 ]
        self._radius = 10 
        self._init_vel = [-2, -2]
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

    def reset(self, screen_dims):
        width, height = screen_dims
        self.coords = [ width // 2, height // 2 ]
        self.velocity = [self.initial_velocity[0] * -1, self.initial_velocity[1]]

    def draw(self, window):
        pygame.draw.circle(window, (255, 255, 255), self.coords, self.radius)

class Player:
    def __init__(self, isTurn, alias, screen_dims):
        self.isTurn = isTurn
        self.paddle = Paddle(isTurn, screen_dims)
        self.name = alias

    def update_paddle_coords(self, height, direction):
        y = self.paddle.y_pos + direction * self.paddle.velocity
        wall_gutters = [ 0, height - self.paddle.height ]
        if wall_gutters[0] < y < wall_gutters[1]:
            self.paddle.y_pos = y
        elif y < wall_gutters[0]:
            self.paddle.y_pos = wall_gutters[0]
        elif y > wall_gutters[1]:
            self.paddle.y_pos = wall_gutters[1] 

class Paddle:
    def __init__(self, isLeft, screen_dims):
        width, height = screen_dims
        self._vel = 4
        self._height = 40
        self._width = 10
        self._gutter_boundary = self.width if isLeft else width - self.width
        self.y_pos = (height - self.height ) // 2
        self._x_pos = 0 if isLeft else width - self.width

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
        pass 

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), (self.x_pos, self.y_pos, self.width, self.height))
