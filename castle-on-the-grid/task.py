#!/bin/python

import math
import os
import random
import re
import sys
from collections import deque

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

def get_rose_of_points(n, grid, source_point):
    rose_of_points = []
    for cursor_x in xrange(0, source_point.x):
        if grid[cursor_x][source_point.y] == 'X':
            break
        rose_of_points.append(Point(cursor_x, source_point.y))
    for cursor_x in xrange(source_point.x + 1, n):
        if grid[cursor_x][source_point.y] == 'X':
            break
        rose_of_points.append(Point(cursor_x, source_point.y))
    for cursor_y in xrange(0, source_point.y):
        if grid[source_point.x][cursor_y] == 'X':
            break
        rose_of_points.append(Point(source_point.x, cursor_y))
    for cursor_y in xrange(source_point.y + 1, n):
        if grid[source_point.x][cursor_y] == 'X':
            break
        rose_of_points.append(Point(source_point.x, cursor_y))
    return rose_of_points

def find_shortest_path(n, grid, start_x, start_y, goal_x, goal_y):
    points_to_visit = deque([Point(start_x, start_y)])
    current_distance = 0
    grid[start_x][start_y] = current_distance
    while len(points_to_visit):
        source_point = points_to_visit.popleft()
        current_distance = grid[source_point.x][source_point.y]
        rose_of_points = get_rose_of_points(n, grid, source_point)
        # print "source_point: " + str(source_point)
        # print "rose_of_points: " + str(map(str, rose_of_points))
        for point in rose_of_points:
            if grid[point.x][point.y] == '.':
                grid[point.x][point.y] = current_distance + 1
                points_to_visit.append(point)
                if point.x == goal_x and point.y == goal_y:
                    # print "grid: \n" + "\n".join(map(lambda row: " ".join(map(str, row)), grid))
                    return current_distance + 1
        # print "grid: \n" + "\n".join(map(lambda row: " ".join(map(str, row)), grid))
    return -1

if __name__ == '__main__':
    n = int(raw_input())

    grid = []

    for _ in xrange(n):
        grid_items = list(raw_input())
        grid.append(grid_items)

    start_x, start_y, goal_x, goal_y = map(int, raw_input().split())
    result = find_shortest_path(n, grid, start_x, start_y, goal_x, goal_y)

    print str(result) + '\n'
