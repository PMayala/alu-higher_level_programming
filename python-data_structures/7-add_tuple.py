#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        x, y = (0, 1)
        tuple_sumx = tuple_a[x] + tuple_b[x]
        tuple_sumy = tuple_a[y] + tuple_b[y]
        return (tuple_sumx, tuple_sumy)
