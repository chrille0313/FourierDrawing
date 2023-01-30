import pygame
from pygame import Vector2
from Model.fourier_model import FourierModel


class FourierDrawer:
    @staticmethod
    def draw(model: FourierModel, window, scale=1):
        window_size = Vector2(window.get_size())
        window_center = Vector2(window_size.x / 2, window_size.y / 2)

        for circle in model.circles:
            pygame.draw.circle(window, circle.color, circle.pos / scale + window_center, circle.amplitude / scale, 1)
            pygame.draw.line(window, circle.color, circle.pos / scale + window_center, circle.get_cartesian_coord(model.time) / scale + window_center, 1)
