#!/usr/bin/python3
"""
Calculates sum from 0 till 200 using top-down and bottom-up recusrsion
"""

import sys

def top_down_sum(i, val, end):
    """
    Calculates sum while moving down in recusrion
    """
    if i > end:
        return val
    return top_down_sum(i + 1, val + i, end)

def bottom_up_sum(i, val, end):
    """
    Calculates sum while moving up in recusrion
    """
    if i == end:
        return i
    else:
        return i + bottom_up_sum(i + 1, val, end)

print("top-down sum[0,200]=" + str(top_down_sum(0, 0, 200)))
print("bottom-up sum[0,200]=" + str(bottom_up_sum(0, 0, 200)))
