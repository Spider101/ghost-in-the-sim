from paddle import Paddle

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

