import numpy.fft
from pygame import Vector2
from numpy import pi, sin, cos, sqrt, arctan2

from Model.FourierCircle import FourierCircle


class FourierModel:
    def __init__(self, signal, position=Vector2(0, 0), rotation=Vector2(0, 0), color=(255, 255, 255)):
        self.signal = signal
        self.pos = position
        self.rotation = rotation
        self.color = color
        self.circles = self.get_circles()

        self.time = 0

    def update(self, dt):
        self.time += dt

        prevCircle: FourierCircle = None
        for circle in self.circles:
            if prevCircle is not None:
                circle.pos = prevCircle.get_cartesian_coord(self.time)

            prevCircle = circle

    def get_circles(self):
        circles = []

        prevCircle: FourierCircle = None
        for frequency, num in enumerate(self.fft()):
            re, im = num.real, num.imag

            amplitude = sqrt(re ** 2 + im ** 2)
            phase = arctan2(im, re)

            circle = FourierCircle(self.pos if prevCircle is None else prevCircle.get_cartesian_coord(0), amplitude, phase, frequency, rotation=self.rotation, color=self.color)
            circles.append(circle)
            prevCircle = circle

        circles.sort(key=lambda c: c.amplitude, reverse=True)

        return circles

    def get_head(self):
        return self.circles[-1].get_cartesian_coord(self.time)

    def fft(self):
        return numpy.fft.fft(self.signal) / len(self.signal)
