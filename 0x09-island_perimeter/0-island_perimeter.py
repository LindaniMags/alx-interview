#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    row_length = len(grid)
    col_length = len(grid[0])
    p = 0
    connect = 0

    for i in range(0, row_length):
        for j in range(0, col_length):
            if grid[i][j] == 1:
                p = p+4

                if i != 0 and grid[i-1][j] == 1:
                    connect = connect+1
                if j != 0 and grid[i][j-1] == 1:
                    connect = connect+1

    return p-(2*connect)
