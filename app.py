import pygame
from pygame import Vector2
from numpy import pi, sin, cos

from Model.PathParser import PathParser

from Model.Path import Path
from Model.fourier_model import FourierModel
from View.fourier_drawer import FourierDrawer


class App:
    def __init__(self):
        self.running = False
        self.window_width, self.window_height = 1920, 1080
        self.window_size = Vector2(self.window_width, self.window_height)
        self.window_center = self.window_size / 2
        self.window = pygame.display.set_mode(self.window_size)

        # image = ImageParser.extract_edges('edges_mod.png')
        # coordinates = ImageParser.convert_to_coordinates(image)
        coordinates = PathParser.get_coords_from_file('data/out.txt')

        image_width = max(x for x, y in coordinates) - min(x for x, y in coordinates)

        signal = [complex(x, y) for x, y in coordinates[::10]]

        self.fourier_model = FourierModel(signal, Vector2(-image_width/2, -self.window_height/2), 0, color=(100, 100, 100))
        self.path = Path()

        self.time = 0

    def init(self):
        pygame.init()

    def run(self):
        self.init()
        clock = pygame.time.Clock()

        self.running = True

        while self.running:
            self.events()
            self.update()
            self.draw()
            clock.tick(60)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
                break

    def update(self):
        dt = 2 * pi / len(self.fourier_model.circles)
        self.time += dt

        if self.time >= 2 * pi:
            self.time = 0
            self.path.reset()

        self.fourier_model.update(dt)
        self.path.add(self.fourier_model.get_head())

    def draw(self):
        self.window.fill((0, 0, 0))
        FourierDrawer.draw(self.fourier_model, self.window, scale=2)
        self.path.draw(self.window, scale=2, color=(9, 205, 218))
        pygame.display.update()

    def quit(self):
        self.running = False


if __name__ == '__main__':
    app = App()
    app.run()
