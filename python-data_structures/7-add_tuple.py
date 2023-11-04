#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Get the first two elements of each tuple or use 0 if the tuple is smaller
    x1, y1 = tuple_a[:2] if len(tuple_a) >= 2 else (0, 0)
    x2, y2 = tuple_b[:2] if len(tuple_b) >= 2 else (0, 0)

    # Calculate the sum of the corresponding elements
    tuple_sum = (x1 + x2, y1 + y2)
    
    return tuple_sum
