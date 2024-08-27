#!/usr/bin/python3
"""
Calculates the perimeter of an island described in the grid
"""


def island_perimeter(grid):
    """find perimeter"""
    per = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # print("[{}][{}] = {}".format(row, col, [row][col]))
            if grid[row][col]:
                # check if island
                # if row == 0 or row == 4 or col == 0 or col == 5:
                #    return per

                # find island boundaries
                if row == 0 or grid[row - 1][col] == 0:
                    per += 1
                if row == (len(grid) - 1) or grid[row + 1][col] == 0:
                    per += 1
                if col == (len(grid[0]) - 1) or grid[row][col + 1] == 0:
                    per += 1
                if col == 0 or grid[row][col - 1] == 0:
                    per += 1
    return per
