import cv2
import numpy as np


class PathParser:
    @staticmethod
    def load_image(path: str):
        return cv2.imread(path)

    @staticmethod
    def extract_edges(path: str):
        image = PathParser.load_image(path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(image, 100, 200)
        return edges

    @staticmethod
    def convert_to_coordinates(edge_image: np.ndarray):
        y, x = np.where(np.all(edge_image == [1, 1, 1], axis=2))
        coordinates = np.column_stack((x, y))

        return coordinates

    @staticmethod
    def get_components(edges: np.ndarray):
        components = cv2.connectedComponents(edges)

        components = components[1]

        return components

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


if __name__ == '__main__':
    """edges = PathParser.extract_edges('../edges_mod.png')
    points = PathParser.convert_to_coordinates(edges)"""

    im = cv2.imread('../edges_mod_connected.png')
    im[im > 0] = 1
    y, x = np.where(np.all(im == [1, 1, 1], axis=2))
    points = np.column_stack((x, y))

    print(points)

    with open("../data/data.txt", "w") as f:
        f.write(f"{len(points)}" + "\n")

        for x, y in points:
            f.write(f"{x},{y}" + "\n")
