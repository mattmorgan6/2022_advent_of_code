import sys

file = sys.argv[1]
# file = 'tempA.in'

with open(file, 'r') as f:
    lines = f.readlines()


class Coord:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z


dirs = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]

cube_coordinates = []
for line in lines:
    x, y, z = line.strip().split(',')
    cube_coordinates.append(Coord(int(x), int(y), int(z)))

size = 30
arr = [[[0 for c in range(30)] for r in range(30)] for q in range(30)]
# ^ put a 0 for unknown, a 1 for rocks, and a -1 for outside air


# PART 1: calculate the surface area of all cubes:


def calc_surface_area():
    surface_area = 0

    for p in cube_coordinates:
        assert not arr[p.x][p.y][p.z]

        arr[p.x][p.y][p.z] = 1
        surface_area += 6

        for dx, dy, dz in dirs:
            nx, ny, nz = p.x + dx, p.y + dy, p.z + dz
            if arr[nx][ny][nz]:
                surface_area -= 2

    return surface_area


inner_surface_area = calc_surface_area()
print(inner_surface_area)
