#!/usr/bin/python3
import sys

def factorial(n):
    """Calculate the factorial of a number.
    
    Args:
        n (int): The number to calculate factorial for
        
    Returns:
        int: The factorial of the input number
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
