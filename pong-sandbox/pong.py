import pygame

from ball import Ball
from player import Player
from score import ScoreCard

class Pong:
    def __init__(self, player_names):
        self._screen_dims = [ 500, 500 ]
        self.ball = Ball(1, self.screen_dims)
        self.player1 = Player(True, player_names[0], self.screen_dims)
        self.player2 = Player(False, player_names[1], self.screen_dims)
        self.score_card= ScoreCard()
    
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
                if x - self.ball.radius <= paddle_gutters[0]:
                    self.score_card.scores[1] += 1
                else:
                    self.score_card.scores[0] += 1

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
        self.score_card.draw(window)
