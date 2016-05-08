#!/usr/bin/python3
"""
Calculates fibonacci numbers
"""

def fibonacci(prev_2, prev_1, i, last):
    if(i > last):
        return prev_1
    fib = prev_2 + prev_1
    return fibonacci(prev_1, fib, i + 1, last)

last = 100
print("fibonacci(100)=" + str(fibonacci(0, 1, 2, last)))
