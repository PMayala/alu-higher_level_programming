#!/usr/bin/python3
def common_elements(set_1, set_2):
    c_set = set_1.intersection(set_2)
#    c_set = []
#    for i, item in enumerate(set_1):
#        if item in set_2:
#            c_set.append(item)
    return c_set
