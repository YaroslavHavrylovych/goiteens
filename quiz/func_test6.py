def new_value(d):
    c = 2
    return mul_values(sum_values(d, 1), c)

def mul_values(a, b):
    return a * b

def sum_values(a, b):
    return a + b

c = new_value(12)
