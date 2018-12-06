#!/bin/python

def sort_with_other_stack(input):
    temp_stack = []
    while len(input):
        temp = input.pop()
        while len(temp_stack) and temp_stack[-1] > temp:
            input.append(temp_stack.pop())
        temp_stack.append(temp)
    return temp_stack

print sort_with_other_stack([2, 10, 8, 3, 5])
