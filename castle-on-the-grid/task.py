#!/bin/python

import math
import os
import random
import re
import sys
from collections import deque
from os import path

DEBUG = False
debug_input = deque([])

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

def get_rose_of_points(n, grid, source_point):
    rose_of_points = []
    for cursor_x in xrange(source_point.x - 1, -1, -1):
        if grid[cursor_x][source_point.y] == 'X':
            break
        rose_of_points.append(Point(cursor_x, source_point.y))
    for cursor_x in xrange(source_point.x + 1, n):
        if grid[cursor_x][source_point.y] == 'X':
            break
        rose_of_points.append(Point(cursor_x, source_point.y))
    for cursor_y in xrange(source_point.y - 1, -1, -1):
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
        if DEBUG:
            print "source_point: " + str(source_point)
            print "rose_of_points: " + str(map(str, rose_of_points))
        for point in rose_of_points:
            if grid[point.x][point.y] == '.':
                grid[point.x][point.y] = current_distance + 1
                points_to_visit.append(point)
                if point.x == goal_x and point.y == goal_y:
                    if DEBUG:
                        print "grid: \n" + "".join(map(lambda row: " ".join(map(str, row)), grid))
                    return current_distance + 1
        if DEBUG:
             print "grid: \n" + "".join(map(lambda row: " ".join(map(str, row)), grid))
             raw_input()
    return -1

def get_input_line():
    if DEBUG:
        return debug_input.popleft()
    return raw_input()

if __name__ == '__main__':

    if DEBUG:
        script_path = path.dirname(__file__)
        print "script_path: " + script_path
        input_path = path.join(script_path, 'input', 'input0.txt')
        f = open(input_path)
        line = f.readline()
        while line:
            debug_input.append(line)
            line = f.readline()

    n = int(get_input_line())

    grid = []

    for _ in xrange(n):
        grid_items = list(get_input_line())
        grid.append(grid_items)

    start_x, start_y, goal_x, goal_y = map(int, get_input_line().split())
    result = find_shortest_path(n, grid, start_x, start_y, goal_x, goal_y)

    print str(result) + '\n'
