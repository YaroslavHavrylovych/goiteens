#!/usr/bin/python3
"""
2 dimentional array contains 0 and 1. Pick a cell  and all 1 and 0 in the vert and horiz becomes
opposite (0 to 1 and 1 to 0). Your task to fill the whole array with 1 (this will open the lock).
"""
import sys
from random import randint

SIZE = 3
LOCK = [[randint(0, 1) for _ in range(SIZE)] for _ in range(SIZE)]

def print_array(array):
    """
    prints lock array to console
    """
    for i in range(SIZE):
        for j in range(SIZE):
            print(" " + str(array[j][i]), end='')
        print()

def read_bounded_int(min_v, max_v, message):
    """
    reads value from the console and check it's in range. In other case re-read those value
    """
    res = None
    while not res:
        try:
            res = int(input(message))
            if res < min_v or res > max_v: 
                if res == -1:
                    print("Exiting...")
                    return None
                print('value has to be less then ' + str(max_v) + ' and greater then ' + str(min_v))
                res = None
            else:
                return res
        except:
            print('Invalid value')

def next_step_to_unlock(array):
    x = read_bounded_int(1, SIZE, "print x (-1 to exit) : ")
    if not x:
        return False
    y = read_bounded_int(1, SIZE, "print y (-1 to exit) : ")
    if not y:
        return False
    x -= 1
    y -= 1
    for i in range(SIZE):
        if i != x:
            array[i][y] = swap_value(array[i][y])
    for i in range(SIZE):
        if i != y:
            array[x][i] = swap_value(array[x][i])
    array[x][y] = swap_value(array[x][y])
    return True

def swap_value(val):
    if val == 1:
        return 0
    else:
        return 1

def solved(array):
    for i in range(SIZE):
        for j in range(SIZE):
            if array[i][j] == 0:
                return False
    return True

def loop():
    while True:
        print_array(LOCK)
        if solved(LOCK):
            break
        if not next_step_to_unlock(LOCK):
            return

    print("You've openned the lock")

print("Your array:")
loop()
