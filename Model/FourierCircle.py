from pygame import Vector2
from numpy import cos, sin


class FourierCircle:
    def __init__(self, pos: Vector2, amplitude: float, phase: float, frequency: float, rotation: float = 0, color=(255, 255, 255)):
        self.pos = pos
        self.rotation = rotation
        self.amplitude = amplitude
        self.phase = phase
        self.frequency = frequency
        self.color = color

    def get_cartesian_coord(self, time: float) -> Vector2:
        phi = self.frequency * time + self.phase + self.rotation
        return Vector2(self.pos.x + cos(phi) * self.amplitude, self.pos.y + sin(phi) * self.amplitude)
