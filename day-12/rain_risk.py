from utils import get_lines
from typing import Tuple
import math
import numpy as np


def move(pos, direct, steps):
    return pos + direct.dot(steps)


def rotation(point, angle):
    angle = angle*math.pi/180
    matrix = np.array([[math.cos(angle), - math.sin(angle)],
                       [math.sin(angle), math.cos(angle)]])
    return np.array(point).dot(matrix)


if __name__ == "__main__":
    data = get_lines('rain_risk.txt')
    data = [(a[0], int(a[1:])) for a in data]
    print(data)

    waypoint = np.array((10, 1))
    position = np.array((0, 0))

    for d, n in data:
        if d == "N":
            waypoint = move(waypoint, np.array((0, 1)), n)
        elif d == "S":
            waypoint = move(waypoint, np.array((0, -1)), n)
        elif d == "E":
            waypoint = move(waypoint, np.array((1, 0)), n)
        elif d == "W":
            waypoint = move(waypoint, np.array((-1, 0)), n)
        elif d == "L":
            waypoint = rotation(waypoint, -n)
        elif d == "R":
            waypoint = rotation(waypoint, n)
        elif d == "F":
            position = move(position, waypoint, n)
        print(d, n, position, waypoint)

    print(round((sum(abs(position)))))
