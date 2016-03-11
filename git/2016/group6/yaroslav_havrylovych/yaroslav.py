"""
Example for your home function
"""

def multiply(value):
    """
    custom progression function
    """
    mul = 1
    for i in range(1, value):
        mul = mul * i
    return mul

print('mul 1..20 = ' + str(multiply(20)))
