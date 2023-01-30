import pygame
from pygame import Vector2


class Path:
    def __init__(self):
        self.path = []

    def add(self, pos):
        self.path.append(pos)

    def reset(self):
        self.path = []

    def draw(self, window, scale=1, color=(255, 255, 255)):
        window_size = Vector2(window.get_size())
        window_center = Vector2(window_size.x / 2, window_size.y / 2)

        for i in range(len(self.path) - 1):
            pygame.draw.line(window, color, self.path[i] / scale + window_center, self.path[i + 1] / scale + window_center, 2)
