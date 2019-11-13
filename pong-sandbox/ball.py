import pygame

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
