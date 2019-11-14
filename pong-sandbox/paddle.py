import pygame

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
