import cv2
import numpy as np


class PathParser:
    @staticmethod
    def load_image(path: str):
        return cv2.imread(path)

    @staticmethod
    def extract_edges(image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(image, 100, 200)
        edges[edges > 0] = 1
        return edges

    @staticmethod
    def convert_to_coordinates(edge_image: np.ndarray):
        y, x = np.where(np.all(edge_image == [1, 1, 1], axis=2))
        coordinates = np.column_stack((x, y))
        return coordinates

    @staticmethod
    def get_coords_from_file(path: str):
        with open(path, 'r') as f:
            lines = f.readlines()

        num_points = int(lines[0])

        points = []

        for i in range(1, num_points + 1):
            x, y = lines[i].split(' ')
            points.append((int(x), int(y)))

        return points

    @staticmethod
    def image_to_path(path: str):
        image = PathParser.load_image(path)
        edges = PathParser.extract_edges(image)
        points = PathParser.convert_to_coordinates(edges)
        return points
