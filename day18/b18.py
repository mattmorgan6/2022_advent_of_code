import sys

"""
Algorithm:

Part 1:
    create a 3-d arr named `arr`
    update arr for each rock subcube
        add 6 - (number of touching faces) to the total surface area
    return total surface area
    
Time Complexity = O(n^3)
Space Complexity = O(n^3)
n = length of one dimension of arr
    
Part 2:
    first, update arr to -1 where a cell is 'outside air'
        we do this by iterating from the top left corner inwards
            if the cell is air and is touching a cell that has value -1, set this cell to -1 also...
        repeat this from the bottom right corner as well
        
    second,
        iterate each cell of arr looking for 'interior air' which has value 0
            if that cell is touching rock (value 1), then subtract 1 from the total exterior area for each face touching 'interior air'   
    
    return total exterior area
    
Time Complexity = O(n^3)
Space Complexity = O(n^3)
n = length of one dimension of arr
"""


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
print("Inner surface area:", inner_surface_area)


# PART 2: find interior pockets of air and subtract them from the exterior_surface_area:


def update_arr_with_outer_air():
    """Work from outside in, updating arr to -1 where the cell is 'outside air'"""
    for x in range(size):
        for y in range(size):
            for z in range(size):
                # Q: how do we know if it is inside the rock?
                # A: we don't, but we will find out if we hit a border
                if x == 0 or y == 0 or z == 0 or x == size - 1 or y == size - 1 or z == size - 1:
                    arr[x][y][z] = -1
                else:
                    if not arr[x][y][z]:
                        for dx, dy, dz in dirs:
                            nx, ny, nz = x + dx, y + dy, z + dz
                            if arr[nx][ny][nz] == -1:
                                arr[x][y][z] = -1
                                break

    for x in range(size - 1, -1, -1):
        for y in range(size -1, -1, -1):
            for z in range(size - 1, -1, -1):
                if x == 0 or y == 0 or z == 0 or x == size - 1 or y == size - 1 or z == size - 1:
                    arr[x][y][z] = -1
                else:
                    if not arr[x][y][z]:
                        for dx, dy, dz in dirs:
                            nx, ny, nz = x + dx, y + dy, z + dz
                            if arr[nx][ny][nz] == -1:
                                arr[x][y][z] = -1
                                break


def calc_air_holes(surface_area):
    for x in range(size):
        for y in range(size):
            for z in range(size):
                if arr[x][y][z] == 0:   # means that it is not outside air and not rock (must be inside air)
                    for dx, dy, dz in dirs:
                        nx, ny, nz = x + dx, y + dy, z + dz
                        assert arr[nx][ny][nz] != -1

                        if arr[nx][ny][nz]:
                            surface_area -= 1

    return surface_area


update_arr_with_outer_air()
outer_surface_area = calc_air_holes(inner_surface_area)
print("Outer surface area:", outer_surface_area)
