#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = []
    result = 0
    for i, item in enumerate(my_list):
        if item not in uniq_list:
            uniq_list.append(item)
            result += item
    return result
